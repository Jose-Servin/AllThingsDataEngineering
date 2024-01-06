from sqlalchemy import create_engine
import pandas as pd


class PostgreSQL:
    def __init__(self, query, connection_url) -> None:
        self.query = query
        self.connection_url = connection_url

    def create_engine(self):
        try:
            engine = create_engine(self.connection_url)
            return engine
        except Exception as e:
            print(f"Error: Unable to create the database engine.\n{e}")
            return None

    def read_sql(self):
        engine = self.create_engine()
        if engine:
            try:
                df = pd.read_sql_query(sql=self.query, con=engine)
                return df
            except Exception as e:
                print(f"Error: Unable to execute SQL query.\n{e}")
                return None
        else:
            return None
