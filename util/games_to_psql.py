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
        password=os.getenv('DB_PASSWORD')
    )

    cursor = conn.cursor()

    for game in games:
        if 'white' in game['players'] and game['players']['white']['user']['id'] == 'dillardchess':
            player_id = game['players']['white']['user']['id']
            player_rating = game['players']['white']['rating']
        elif 'black' in game['players'] and game['players']['black']['user']['id'] == 'dillardchess':
            player_id = game['players']['black']['user']['id']
            player_rating = game['players']['black']['rating']
        else:
            continue

        insert_query = sql.SQL("""
            INSERT INTO Games (id, created_at, status, player_id, player_rating, winner, opening)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """)

        cursor.execute(insert_query, (
            game['id'],
            game['createdAt'],
            game['status'],
            player_id,
            player_rating,
            game.get('winner', None),
            game['opening']['name'] if 'opening' in game else None
        ))

    conn.commit()
    cursor.close()
    conn.close()

games = get_games()
insert_games(games)
