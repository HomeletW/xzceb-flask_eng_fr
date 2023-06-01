import unittest
from machinetranslation import translator


class MachineTranslationTest(unittest.TestCase):
    def test_english_to_french_hello(self):
        self.assertEqual(translator.englishToFrench("hello"), "bonjour")

    def test_french_to_english_hello(self):
        self.assertEqual(translator.frenchToEnglish("bonjour"), "hello")

    def test_english_to_french_longer_text(self):
        self.assertEqual(translator.englishToFrench("Hello world and I love programming"), "Bonjour le monde et j'adore la programmation")

    def test_french_to_english_longer_text(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour le monde et j'adore la programmation"), "Hello world and I love programming")

if __name__ == "__main__":
    unittest.main()