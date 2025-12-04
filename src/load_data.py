import pandas as pd
import sqlite3

def load_from_csv(path):
    return pd.read_csv(path)

def load_from_sqlite(db_path, table_name="hive_trials"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df