import unittest

def calc_square(num):
    if not isinstance(num, int, float):
        raise TypeError(f"{num} must be an integer or a float.")
    return num**num

class TestSquare(unittest.TestCase):
    def test_correct_input(self):
        result = calc_square(4)
        self.assertEqual(result, 16)
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calc_square("5")
        with self.assertRaises(TypeError):
            calc_square([5])
        with self.assertRaises(TypeError):
            calc_square({5})

if __name__ == "__main__":
    unittest.main()

