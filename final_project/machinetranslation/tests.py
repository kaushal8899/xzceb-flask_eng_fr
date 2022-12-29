import unittest
from translator import englishToFrench,frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish(None),None)
        self.assertEqual(englishToFrench(None),None)

unittest.main()