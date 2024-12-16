import psycopg2
import psycopg2.extras
from ..settings import DB_CONFIG


def get_hotels():
    query = """
    SELECT hotel_id, place
    FROM hotels
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def get_affilations():
    query = """
    SELECT affilation_id, name
    FROM affilations
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()