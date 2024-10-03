# 1. wczytanie danych z plików csv
# 2. utworzenie bazy danych SQLite
# 3. załadowanie danych z csv do bazy danych

import pandas as pd
from sqlalchemy import create_engine, text

# Ścieżki do plików CSV
stations_csv = "clean_stations.csv"
measures_csv = "clean_measure.csv"

# Wczytanie danych z CSV do DataFrame'ów
stations_df = pd.read_csv(stations_csv)
measures_df = pd.read_csv(measures_csv)

# Utworzenie silnika bazodanowego SQLite
engine = create_engine('sqlite:///weather_data.db')

# Załadowanie danych do tabel SQLite
# "if_exists='replace'" oznacza, że tabela zostanie nadpisana, jeśli istnieje
stations_df.to_sql('stations', con=engine, if_exists='replace', index=False)
measures_df.to_sql('measures', con=engine, if_exists='replace', index=False)

# Sprawdzenie, czy dane zostały poprawnie załadowane
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM stations LIMIT 5")).fetchall()
    print("Stations:", result)
    
    result = conn.execute(text("SELECT * FROM measures LIMIT 5")).fetchall()
    print("Measures:", result)