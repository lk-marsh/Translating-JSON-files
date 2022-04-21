import boto3


# Outputs a translated string given an input string, source and target languages. Source language defaults to English.
def translate(text: str, target_language_code: str, source_language_code: str) -> str:

    translate = boto3.client(
        service_name='translate',
        region_name='ap-southeast-1',
        use_ssl=True
    )
    result = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
    )

    return result.get('TranslatedText')
