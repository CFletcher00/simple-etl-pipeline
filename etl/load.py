import sqlite3

def load(df, db_path, table_name="transactions"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="append", index=False)
    conn.close()
