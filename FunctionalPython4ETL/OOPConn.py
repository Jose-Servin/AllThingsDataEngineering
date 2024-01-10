from Classes.SQL import PostgreSQL
from Classes.Loads import Loads
# from config import CONNECTION_URL
from Queries.customer_query import CUSTOMER_5524
import pandas as pd
import sys
import configparser

# Load Config
config = configparser.ConfigParser()
config.read("./Config/config.ini")

connection_url = config['Dev']['CONNECTION_URL']
extract_path = config['Dev']['EXTRACT_PATH']

postgres_instance = PostgreSQL(CUSTOMER_5524, connection_url)
result_df = postgres_instance.read_sql()

if result_df is not None:
    print(result_df)
else:
    print("Failed to fetch data.")
