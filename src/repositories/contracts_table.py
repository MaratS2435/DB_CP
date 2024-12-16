import psycopg2
import psycopg2.extras
import streamlit as st
from ..settings import DB_CONFIG

def get_contracts_table(my = False):
    if my:
        query = """
        SELECT contract_id, task
        FROM contracts
        WHERE client_id = %(user_id)s
        ORDER BY contract_id
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(query, {"user_id": st.session_state.user_id})
                return cur.fetchall()
    else:
        query = """
        SELECT contract_id, task, users.name, reward 
        FROM contracts
             LEFT JOIN
             users
             ON contracts.client_id = users.user_id
        WHERE task_id != %(user_id)s OR task_id IS NULL
        ORDER BY contract_id
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, {"user_id": st.session_state.user_id})
                return cur.fetchall()

def put_contract(task, reward, task_name = None):
    task_id = None
    if task_name is not None:
        query1 = """
        SELECT user_id
        FROM users
        WHERE name = %(task_name)s 
        """

    query2 = """
    INSERT INTO contracts (task, task_id, reward, client_id)
    VALUES (%(task)s, %(task_id)s, %(reward)s, %(user_id)s)
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            if task_name is not None:
                cur.execute(query1, {"task_name": task_name})
                result = cur.fetchone()
                if result is None:
                    task_id = None
                else:
                    task_id = result[0]
            cur.execute(query2, {"task": task, "task_id": task_id, "reward": reward, "user_id": st.session_state.user_id})
            conn.commit()

def delete_contract(contract_id):
    query_1 = """
        DELETE FROM contracts_executers
        WHERE contract_id = %(contract_id)s
        """

    query_2 = """
    DELETE FROM contracts
    WHERE contract_id = %(contract_id)s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query_1, {"contract_id": contract_id})
            cur.execute(query_2, {"contract_id": contract_id})
            conn.commit()

def make_executer(contract_id, executer_id):
    query_check_1 = """
    SELECT contract_id
    FROM contracts
    WHERE contract_id = %(contract_id)s
    """

    query_check_2 = """
    SELECT contract_id, executer_id
    FROM contracts_executers
    WHERE contract_id = %(contract_id)s
          AND executer_id = %(executer_id)s
    """

    query = """
    INSERT INTO contracts_executers (contract_id, executer_id)
    VALUES (%(contract_id)s, %(executer_id)s)
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query_check_1, {"contract_id": contract_id})
            result = cur.fetchone()
            if result is None:
                return 1

            cur.execute(query_check_2, {"contract_id": contract_id, "executer_id": executer_id})
            result = cur.fetchone()
            if result is not None:
                return 2

            cur.execute(query, {"contract_id": contract_id, "executer_id": st.session_state.user_id})
            conn.commit()

def my_contracts():
    contracts = get_contracts_table(my=True)
    return {contract["task"]: contract["contract_id"] for contract in contracts}