import unittest
import molecule_syntax as ms


class SyntaxTest(unittest.TestCase):

    def test_sampleInputOne(self):
        """Tests the result when given correct input data"""
        self.assertEqual(ms.check_syntax("Na"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(ms.check_syntax("H2O"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(ms.check_syntax("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(ms.check_syntax("Na332"), "Formeln är syntaktiskt korrekt")

    def test_sampleInputTwo(self):
        """Tests the result when given incorrect input data"""
        self.assertEqual(ms.check_syntax("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
        self.assertEqual(ms.check_syntax("C(OH4)C"), "Saknad siffra vid radslutet C")
        self.assertEqual(ms.check_syntax("C(OH4C"), "Saknad högerparentes vid radslutet")
        self.assertEqual(ms.check_syntax("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")
        self.assertEqual(ms.check_syntax("H0"), "För litet tal vid radslutet")
        self.assertEqual(ms.check_syntax("H1C"), "För litet tal vid radslutet C")
        self.assertEqual(ms.check_syntax("H02C"), "För litet tal vid radslutet 2C")
        self.assertEqual(ms.check_syntax("Nacl"), "Saknad stor bokstav vid radslutet cl")
        self.assertEqual(ms.check_syntax("a"), "Saknad stor bokstav vid radslutet a")
        self.assertEqual(ms.check_syntax("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
        self.assertEqual(ms.check_syntax(")"), "Felaktig gruppstart vid radslutet )")
        self.assertEqual(ms.check_syntax("2"), "Felaktig gruppstart vid radslutet 2")


if __name__ == '__main__':
    unittest.main()
