import unittest
import numpy as np
import pandas as pd;

class PandasOperations(unittest.TestCase):



    def test_pandas(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
        print(df.head())
        # unique values
        print(df['col2'].unique())
        # unique value count
        print(df['col2'].value_counts())
        # selecting values or querying
        newdf = df[(df['col1'] > 2) & (df['col2'] == 444)]
        print(newdf)
        #applying functions
        print(df['col1'].apply(self.times2))
        #getting the sum
        print(df['col1'].sum())

        #deleting a column
        del df['col1']
        print(df)

        #get the columns
        print(df.columns)

        #drop null values
        print(df.isnull())

        df.dropna()

        # filling null values with some other values
        df2 = pd.DataFrame({'col1': [1, 2, 3, np.nan],
                           'col2': [np.nan, 555, 666, 444],
                           'col3': ['abc', 'def', 'ghi', 'xyz']})

        print(df2.head())
        print(df2.fillna('FILL'))


    def times2(self,x):
        return x * 2



