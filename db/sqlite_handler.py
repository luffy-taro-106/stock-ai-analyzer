
import sqlite3

def store_to_db(df, table_name="stock_data", db_path="db/stock.sqlite"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

