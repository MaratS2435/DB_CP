import psycopg2
import bcrypt
import streamlit as st
from ..settings import DB_CONFIG

def put_user(name, password, age, status, role, hotel_id, affilation_id):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    query = """
    INSERT INTO users (name, password, age, status, role, hotel_id, affilation_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    RETURNING user_id 
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, hashed_password, age, status, role, hotel_id, affilation_id))
            conn.commit()
            user_id = cur.fetchone()[0]
            return user_id

def edit_user(user_id, option, new_value):
    query_check = """
    SELECT user_id
    FROM users
    WHERE user_id = %(user_id)s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query_check, {"user_id": user_id})
            result = cur.fetchone()
            if result is None:
                st.warning("User not found")
                return

    if option == "status":
        query = """
        UPDATE users
        SET status = %(status)s
        WHERE user_id = %(user_id)s
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, {"status": new_value, "user_id": user_id})
                conn.commit()

    elif option == "role":
        query = """
        UPDATE users
        SET role = %(role)s
        WHERE user_id = %(user_id)s
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, {"role": new_value, "user_id": user_id})
                conn.commit()

    elif option == "hotel_id":
        query = """
        UPDATE users
        SET hotel_id = %(hotel_id)s
        WHERE user_id = %(user_id)s
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, {"hotel_id": new_value, "user_id": user_id})
                conn.commit()

    elif option == "affilation_id":
        query = """
        UPDATE users
        SET affilation_id = %(affilation_id)s
        WHERE user_id = %(user_id)s
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, {"affilation_id": new_value, "user_id": user_id})
                conn.commit()

def get_users(hotel_id = None):
    if hotel_id is not None:
        query = """
        SELECT user_id, name, age, status, role, hotel_id, affilation_id
        FROM users
        WHERE hotel_id = %(hotel_id)s
        ORDER BY user_id
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, {"hotel_id": hotel_id})
                return cur.fetchall()
    else:
        query = """
        SELECT user_id, users.name, age, status, role, hotels.place, affilations.name
        FROM users
             LEFT JOIN
             hotels
             ON users.hotel_id = hotels.hotel_id
             LEFT JOIN
             affilations
             ON users.affilation_id = affilations.affilation_id
        ORDER BY user_id
        """
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()