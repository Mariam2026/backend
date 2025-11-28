import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="EventPlanner",     # database name
        user="postgres",              # PostgreSQL username
        password="mariam",
        host="localhost",
        port="5432"
    )
