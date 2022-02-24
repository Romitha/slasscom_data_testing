from util.RunQuery import RunQuery
import unittest
import os

config_file_path = os.path.join(os.getcwd(), 'config', r'config.ini')

class DBTest(unittest.TestCase):

    def test_db_connection(self):

        sql = """
                select pid as process_id
                from pg_stat_activity;
            """
        db = "free_db"
        df4 = RunQuery(sql, db, config_file_path).executeQueryWithRawSql()
        print(df4)
        self.assertEqual(1, 1)

    def test_something_else(self):
        sql = "select * from diabetes_csv"
        db = "free_db"
        df = RunQuery(sql, db, config_file_path).executeQuery()
        print(df.head(10))
        duplicateRows = df[df.duplicated()]

        self.assertEqual(duplicateRows.shape[0], 0)
