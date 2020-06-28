import unittest
import adding

class TestBasic(unittest.TestCase):
    def test_me(self):
        self.assertEqual(adding.add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
