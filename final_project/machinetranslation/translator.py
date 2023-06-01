'''
Translator module
'''

from deep_translator import MyMemoryTranslator


def englishToFrench(englisht_text):
    '''
    Return the french translation of the english text.
    '''
    french_text = MyMemoryTranslator(source='en', target='fr').translate(englisht_text)
    return french_text


def frenchToEnglish(french_text):
    '''
    Return the english translation of the french text.
    '''
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
