import unittest

import matplotlib
import numpy as np
import pandas as pd


class MatPlotOperations(unittest.TestCase):

    def test_data_visulization(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
        print(df['col1'].hist())
