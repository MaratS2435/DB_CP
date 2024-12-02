import psycopg2
import psycopg2.extras
import streamlit as st
from ..settings import DB_CONFIG

def get_excommunicado(user_id):
    query = """
    SELECT rules.description, reward, begining
    FROM excommunicados
         LEFT JOIN 
         rules
    ON excommunicados.rule_id = rules.rule_id
    WHERE user_id = %(user_id)s
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"user_id": user_id})
            return cur.fetchone()

def get_excommunicados():
    query = """
    WITH
    descripted_rules AS (
        SELECT user_id, rules.description, reward, begining
        FROM excommunicados
             LEFT JOIN 
             rules
        ON excommunicados.rule_id = rules.rule_id
    ),
    named_excommunicados AS (
        SELECT users.name, description, reward, begining
        FROM descripted_rules
             LEFT JOIN 
             users
        ON descripted_rules.user_id = users.user_id
    )
    
    SELECT name, description, reward, begining
    FROM named_excommunicados
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

def put_excommunicado(user_id, rule_id, reward, begining):
    query_check = """
    SELECT user_id
    FROM excommunicados
    WHERE user_id = %(user_id)s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query_check, {"user_id": user_id})
            result = cur.fetchone()
            if result is not None:
                st.warning("User is already excommunicated")
                return

    query = """
    INSERT INTO excommunicados (user_id, rule_id, reward, begining)
    VALUES (%(user_id)s, %(rule_id)s, %(reward)s, %(begining)s)
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"user_id": user_id, "rule_id": rule_id, "reward": reward, "begining": begining})
            conn.commit()
            st.success("User excommunicated successfully!")

def edit_excommunicado_reward(user_id, new_reward):
    query_check = """
    SELECT user_id
    FROM excommunicados
    WHERE user_id = %(user_id)s
    """

    with psycopg2.connect(**DB_CONFIG).get_connection as conn:
        with conn.cursor() as cur:
            cur.execute(query_check, {"user_id": user_id})
            result = cur.fetchall()
            if result is None:
                st.warning("User isn't excommunicated")

    query = """
    UPDATE excommunicados
    SET reward = %(reward)s
    WHERE user_id = %(user_id)s
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"reward": new_reward, "user_id": user_id})
            conn.commit()
            st.success("Reward updated successfully!")


def get_rules():
    query = """
    SELECT rule_id, description
    FROM rules
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()
