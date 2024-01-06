from Classes.SQL import PostgreSQL
from config import CONNECTION_URL

query = "select customer_id, year_birth, education from master_data where customer_id = 5524"
connection_url = CONNECTION_URL


postgres_instance = PostgreSQL(query, connection_url)
result_df = postgres_instance.read_sql()

if result_df is not None:
    print(result_df)
else:
    print("Failed to fetch data.")
