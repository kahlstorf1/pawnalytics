import os
import pandas as pd
from sqlalchemy import create_engine
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

def get_games_from_db():
    engine = create_engine(f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@localhost/{os.getenv("DB_DB")}')
    df = pd.read_sql('SELECT * FROM Games', con=engine)
    return df

# Getting the data
df = get_games_from_db()

# Setting the index and sorting
df['created_at'] = pd.to_datetime(df['created_at'])
df.set_index('created_at', inplace=True)
df.sort_index(inplace=True)

# Simple plot of player's rating over time
df['player_rating'].plot()
plt.show()

# Fit an ARIMA(5,1,0) model
model = ARIMA(df['player_rating'], order=(5,1,0))
model_fit = model.fit(disp=0)

# Print a summary of the model
print(model_fit.summary())

# Plot the residuals
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
plt.show()

# Plot the density of the residuals
residuals.plot(kind='kde')
plt.show()

# Print some stats on the residuals
print(residuals.describe())
