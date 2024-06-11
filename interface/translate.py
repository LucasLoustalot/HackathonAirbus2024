from deep_translator import GoogleTranslator

langs = [
    "afrikaans",
    "albanian",
    "amharic",
    "arabic",
    "armenian",
    "assamese",
    "aymara",
    "azerbaijani",
    "bambara",
    "basque",
    "belarusian",
    "bengali",
    "bhojpuri",
    "bosnian",
    "bulgarian",
    "catalan",
    "cebuano",
    "chichewa",
    "chinese (simplified)",
    "chinese (traditional)",
    "corsican",
    "croatian",
    "czech",
    "danish",
    "dhivehi",
    "dogri",
    "dutch",
    "english",
    "esperanto",
    "estonian",
    "ewe",
    "filipino",
    "finnish",
    "french",
    "frisian",
    "galician",
    "georgian",
    "german",
    "greek",
    "guarani",
    "gujarati",
    "haitian creole",
    "hausa",
    "hawaiian",
    "hebrew",
    "hindi",
    "hmong",
    "hungarian",
    "icelandic",
    "igbo",
    "ilocano",
    "indonesian",
    "irish",
    "italian",
    "japanese",
    "javanese",
    "kannada",
    "kazakh",
    "khmer",
    "kinyarwanda",
    "konkani",
    "korean",
    "krio",
    "kurdish (kurmanji)",
    "kurdish (sorani)",
    "kyrgyz",
    "lao",
    "latin",
    "latvian",
    "lingala",
    "lithuanian",
    "luganda",
    "luxembourgish",
    "macedonian",
    "maithili",
    "malagasy",
    "malay",
    "malayalam",
    "maltese",
    "maori",
    "marathi",
    "meiteilon (manipuri)",
    "mizo",
    "mongolian",
    "myanmar",
    "nepali",
    "norwegian",
    "odia (oriya)",
    "oromo",
    "pashto",
    "persian",
    "polish",
    "portuguese",
    "punjabi",
    "quechua",
    "romanian",
    "russian",
    "samoan",
    "sanskrit",
    "scots gaelic",
    "sepedi",
    "serbian",
    "sesotho",
    "shona",
    "sindhi",
    "sinhala",
    "slovak",
    "slovenian",
    "somali",
    "spanish",
    "sundanese",
    "swahili",
    "swedish",
    "tajik",
    "tamil",
    "tatar",
    "telugu",
    "thai",
    "tigrinya",
    "tsonga",
    "turkish",
    "turkmen",
    "twi",
    "ukrainian",
    "urdu",
    "uyghur",
    "uzbek",
    "vietnamese",
    "welsh",
    "xhosa",
    "yiddish",
    "yoruba",
    "zulu",
]


def get_translated_list(word):
    data = []
    for lang in langs:
        translated = GoogleTranslator(source="auto", target=lang).translate(text=word)
        if translated != word:
            translate_details = {
                "lang": lang,
                "translation": translated,
            }
            data.append(translate_details)
    return data


print(get_translated_list("Bonjour")[0]["lang"])
