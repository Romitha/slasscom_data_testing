from util.DBConnection import DBConnection
import psycopg2
import pandas as pd
class RunQuery:

    def __init__(self, query, db, config_path):
        self.query = query
        self.db = db
        self.config_path = config_path

    def executeQuery(self):
        connection = None

        try:
            connection = DBConnection(None, self.db, self.config_path).create_connection()
            df = pd.read_sql_query(self.query, connection)
            return df

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            return pd.DataFrame()
        finally:
            if connection:
                connection.close()

    def executeQueryWithRawSql(self):
        connection = None
        try:
            connection = DBConnection(None, self.db, self.config_path).create_connection()
            curs = connection.cursor()
            curs.execute(self.query)
            result = curs.fetchall()
            return result

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                connection.close()