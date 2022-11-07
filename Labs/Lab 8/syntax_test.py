import unittest
import molecule_syntax as ms


class SyntaxTest(unittest.TestCase):

    def test_validInput(self):
        """Tests the result when given correct input data"""
        self.assertEqual(ms.check_syntax("H10100"), "Formeln är syntaktiskt korrekt")

    def test_invalidInput(self):
        """Tests the result when given incorrect input data"""
        self.assertEqual(ms.check_syntax("H01011"), "För litet tal vid radslutet 1011")

if __name__ == '__main__':
    unittest.main()
