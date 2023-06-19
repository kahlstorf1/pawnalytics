import os
import psycopg2
from psycopg2 import sql

from get_games import get_games
from dotenv import load_dotenv

load_dotenv()

def insert_games(games):
    conn = psycopg2.connect(
        host="localhost",
        database=os.getenv('DB_DB'),
        user=os.getenv('DB_USER'),
        password=""
    )

    cursor = conn.cursor()

    for game in games:
        insert = sql.SQL("INSERT INTO games (id, created_at) VALUES (%s, %s)")
        values = (game['id'], game['createdAt'])

        cursor.execute(insert, values)

    conn.commit()
    cursor.close()
    conn.close()

games = get_games()
insert_games(games)
