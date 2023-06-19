import os
from dotenv import load_dotenv
import berserk
from datetime import datetime

load_dotenv()

def get_games():
  session = berserk.TokenSession(os.getenv('API_KEY'))
  client = berserk.Client(session)

  start = berserk.utils.to_millis(datetime(2020, 12, 8))
  end = berserk.utils.to_millis(datetime(2021, 12, 9))
  games = client.games.export_by_player('dillardchess', since=start, until=end, opening=True, max=30)

  return games
