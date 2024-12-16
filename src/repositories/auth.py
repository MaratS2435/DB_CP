import bcrypt
import psycopg2
from ..settings import DB_CONFIG

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def check_excommunicado(user_id):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM excommunicados WHERE user_id = %s", (user_id,))
            return cur.fetchone() is not None

def authenticate(user_id, password):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id, password, role FROM users WHERE user_id = %s", (user_id,))
            user = cur.fetchone()
            if not user:
                return None
            user_id, hashed_password = user[0], user[1]
            if not verify_password(password, hashed_password):
                return None
            return {"user_id": user_id, "role": user[2]}
