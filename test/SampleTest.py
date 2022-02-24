import unittest


class Testing(unittest.TestCase):

    def setUp(self):
        print("........set up is called ..........")

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = False
        self.assertEqual(a, b)



    def tearDown(self):
        print("........tear down is called ..........")

# if __name__ == '__main__':
#     unittest.main()