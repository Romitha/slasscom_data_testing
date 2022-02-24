import unittest

import matplotlib
import numpy as np
import pandas as pd
import datatest as dt


class TestMovies(unittest.TestCase):

    def setUp(self):
        print("........set up is called ..........")
        global df
        with dt.working_directory(__file__):
            df = pd.read_csv('../data/movies.csv')
            print(df)


    def test_coulmn_values(self):
        dt.validate(
            df.columns,
            {'title', 'rating', 'year', 'runtime'},"Columns not matching"
        )

    def test_title(self):
        dt.validate.regex(df['title'], r'^[A-Z]')

    def test_rating(self):
        dt.validate.superset(
            df['rating'],
            {'G', 'PG', 'PG-13', 'R', 'NC-17', 'Not Rated'},"values should match"
        )

    def test_year(self):
       dt.validate(df['year'], int,"should be in integer")

    def test_runtime(self):
        dt.validate(df['runtime'], int)
