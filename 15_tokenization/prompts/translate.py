import asyncio
from googletrans import Translator

async def translate_to_french(text_to_translate):
    """
    Translates the given text from English to French using Google Translate.

    Args:
        text_to_translate (str): The English text to be translated.

    Returns:
        str: The translated French text, or an error message if translation fails.
    """
    translator = Translator()
    try:
        # 'src' specifies the source language (English in this case)
        # 'dest' specifies the destination language (French 'fr')
        translation = await translator.translate(text_to_translate, src='en', dest='fr')
        return translation.text
    except Exception as e:
        return f"An error occurred during translation: {e}"

async def main():
    # The text you want to translate
    english_text = "My Name is Pulkit Gupta?"

    # Perform the translation
    french_translation = await translate_to_french(english_text)

    # Print the results
    print(f"Original English Text: {english_text}")
    print(f"Translated French Text: {french_translation}")

if __name__ == "__main__":
    asyncio.run(main())