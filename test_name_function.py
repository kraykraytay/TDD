import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):

    def test_last_first_name(self):
        result = formatted_name("potter", "harry")
        self.assertEqual(result, "Potter, Harry")

    def test_other_last_first_name(self):
        result = formatted_name("granger", "hermoine")
        self.assertEqual(result, "Granger, Hermoine")

    def test_last_first_middle_name(self):
        result = formatted_name("potter", "albus", "severus")
        self.assertEqual(result, "Potter, Albus Severus")



if __name__ == '__main__':
    unittest.main()