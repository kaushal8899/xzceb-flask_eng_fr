"""
    Module to translate from English to French and French to English
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#language_translator.set_disable_ssl_verification(True)

def englishToFrench(english_text):
    """
        Translate from English to French
    """
    #write the code here
    if english_text is None:
        return None
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    #write the code here
    """
        Translate from French to English
    """
    if french_text is None:
        return None
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
