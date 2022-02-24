import unittest
import numpy as np


class NumpyOperations(unittest.TestCase):

    def test_numpy(self):
        arr = np.arange(0, 10)
        print(arr)
        print(np.zeros((2, 3)))
        print(np.ones((2, 3)))
        print(np.linspace(0, 5, 100))

    def test_numpy_operations(self):
        arr = np.arange(0, 10)
        print(arr+100)
        print(arr**100)
        print(np.sqrt(arr))

