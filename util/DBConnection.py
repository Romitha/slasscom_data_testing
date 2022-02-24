import psycopg2
from util.ConfigReader import ConfigReader


class DBConnection:
    def __init__(self, query, db, config_path):
        self.query = query
        self.db = db
        self.config_path = config_path


    def create_connection(self):
        config = ConfigReader().load_config(self.config_path)
        dbname = config[self.db]["dbname"]
        host = config[self.db]["host"]
        port = config[self.db]["port"]
        userName = config[self.db]["user"]
        password = config[self.db]["pass"]


        try:
            # Connect to an existing database
            connection = psycopg2.connect(user=userName,
                                        password=password,
                                        host=host,
                                        port=port,
                                        database=dbname)

            # print("PostgreSQL server information {}".format(connection))
            return connection

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)