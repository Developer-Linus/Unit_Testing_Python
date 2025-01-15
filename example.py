import unittest

def add(x,y):
    return x+y

class TestAdd(unittest.TestCase):

    def test_add_positive(self):
        result = add(5,3)
        self.assertEqual(result, 8)

    def test_add_negative(self):
        result = add(-1, 7)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()

