from util.RunQuery import RunQuery
import unittest
import os
import pandasql as ps
import functools
import findspark
import os

findspark.init()
import pyspark  # only run after findspark.init()

from pyspark import SparkContext
from pyspark import SparkFiles
from pyspark.sql import Row
from pyspark.sql import SQLContext

# Import all from `sql.types`
from pyspark.sql.types import *

sc = SparkContext()
url = "https://raw.githubusercontent.com/guru99-edu/R-Programming/master/adult_data.csv"


class SparkTest(unittest.TestCase):

    def test_pyspark(self):
        sc.addFile(url)
        sqlContext = SQLContext(sc)
        df = sqlContext.read.csv(SparkFiles.get("adult_data.csv"), header=True, inferSchema=True)
        print(df.printSchema())
        self.assertEqual(2, 2)

    # Write a custom function to convert the data type of DataFrame columns
    @staticmethod
    def convertColumn(df, names, newType):
        for name in names:
            df = df.withColumn(name, df[name].cast(newType))
        return df

    def test_pysaprk_column_type(self):
        sc.addFile(url)
        sqlContext = SQLContext(sc)
        df = sqlContext.read.csv(SparkFiles.get("adult_data.csv"), header=True, inferSchema=True)
        # List of continuous features
        CONTI_FEATURES = ['age', 'fnlwgt', 'capital-gain', 'educational-num', 'capital-loss', 'hours-per-week']
        # Convert the type
        df = SparkTest.convertColumn(df, CONTI_FEATURES, FloatType())
        df = df.withColumnRenamed("capital-gain", "capital_gain").withColumnRenamed("educational-num", "educational_num").withColumnRenamed("capital-loss", "capital_loss").withColumnRenamed("hours-per-week", "hours_per_week").withColumnRenamed("native-country", "native_country")
        # Check the dataset
        print(df.printSchema())
        print(df.show())

        self.assertEqual(df.filter(df.native_country == 'Holand-Netherlands').count(), 1)
