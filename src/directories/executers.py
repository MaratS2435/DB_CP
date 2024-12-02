import psycopg2
import psycopg2.extras
from ..settings import DB_CONFIG


def get_executers(contract_id):
    query = """
    SELECT users.name
    FROM contracts_executers
         LEFT JOIN
         users
         ON contracts_executers.executer_id = users.user_id
    WHERE contracts_executers.contract_id = %(contract_id)s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, {"contract_id": contract_id})
            return cur.fetchall()