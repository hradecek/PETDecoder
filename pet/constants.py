# -*- coding: utf-8 -*-
"""
This module contains only constants defined in various IPMI specifications.
"""
import datetime

"""
Start of PET local timestamp as defined in Platform Event Trap Format Specification v1.0,
Table 3 - Variable Bindings Fields.

See: https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/platform-event-trap.pdf
"""
PET_EPOCH = datetime.datetime(day=1, month=1, year=1998)

"""
Event/Trap source types as defined in Platform Event Trap Format Specification v1.0, Table 3 - Variable Bindings Fields.

See: https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/platform-event-trap.pdf
"""
SOURCE_TYPES = {
    range(0x00, 0x07): 'Platform Firmware (e.g. BIOS)',
    range(0x08, 0x0F): 'SMI Handler',
    range(0x10, 0x17): 'ISV System Management Software',
    range(0x18, 0x1F): 'Alert ASIC',
    range(0x20, 0x27): 'IPMI',
    range(0x28, 0x2F): 'BIOS Vendor',
    range(0x30, 0x37): 'System Board Set Vendor',
    range(0x38, 0x3F): 'System Integrator',
    range(0x40, 0x47): 'Third Party Add-in',
    range(0x48, 0x4F): 'OSV',
    range(0x50, 0x57): 'NIC',
    range(0x58, 0x5F): 'System Management Card'
}

"""
PET severity types as defined in Platform Event Trap Format Specification v1.0, Table 3 - Variable Bindings Fields.

See: https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/platform-event-trap.pdf
"""
SEVERITY_TYPES = {
    0x01: 'Monitor',
    0x02: 'Information',
    0x04: 'OK',
    0x08: 'Non-critical condition (a.k.a. warning)',
    0x10: 'Critical condition',
    0x20: 'Non-recoverable condition'
}

"""
Language codes as defined in Platform Management FRU Information Storage Definition v1.0, Table 15-1, Language codes

See: https://www.intel.com/content/dam/www/public/us/en/documents/specification-updates/ipmi-platform-mgt-fru-info-storage-def-v1-0-rev-1-3-spec-update.pdf
"""
LANGUAGE_CODES = {
    0: 'en English',
    1: 'aa Afar', 51: 'it Italian', 101: 'si Singhalese',
    2: 'ab Abkhazian', 52: 'iw Hebrew', 102: 'sk Slovak',
    3: 'af Afrikaans', 53: 'ja Japanese', 103: 'sl Slovenian',
    4: 'am Amharic', 54: 'ji Yiddish', 104: 'sm Samoan',
    5: 'ar Arabic', 55: 'jw Javanese 105: sn Shona',
    6: 'as Assamese', 56: 'ka Georgian 106: so Somali',
    7: 'ay Aymara', 57: 'kk Kazakh 107: sq Albanian',
    8: 'az Azerbaijani', 58: 'kl Greenlandic 108: sr Serbian',
    9: 'ba Bashkir', 59: 'km Cambodian 109: ss Siswati',
    10: 'be Byelorussian', 60: 'kn Kannada', 110: 'st Sesotho',
    11: 'bg Bulgarian', 61: 'ko Korean', 111: 'su Sudanese',
    12: 'bh Bihari', 62: 'ks Kashmiri', 112: 'sv Swedish',
    13: 'bi Bislama', 63: 'ku Kurdish', 113: 'sw Swahili',
    14: 'bn Bengali; Bangla', 64: 'ky Kirghiz', 114: 'ta Tamil',
    15: 'bo Tibetan', 65: 'la Latin', 115: 'te Tegulu',
    16: 'br Breton', 66: 'ln Lingala', 116: 'tg Tajik',
    17: 'ca Catalan', 67: 'lo Laothian', 117: 'th Thai',
    18: 'co Corsican', 68: 'lt Lithuanian', 118: 'ti Tigrinya',
    19: 'cs Czech', 69: 'lv Latvian, Lettish', 119: 'tk Turkmen',
    20: 'cy Welsh', 70: 'mg Malagasy', 120: 'tl Tagalog',
    21: 'da danish', 71: 'mi Maori', 121: 'tn Setswana',
    22: 'de german', 72: 'mk Macedonian', 122: 'to Tonga',
    23: 'dz Bhutani', 73: 'ml Malayalam', 123: 'tr Turkish',
    24: 'el Greek', 74: 'mn Mongolian', 124: 'ts Tsonga',
    25: 'en English', 75: 'mo Moldavian', 125: 'tt Tatar',
    26: 'eo Esperanto', 76: 'mr Marathi', 126: 'tw Twi',
    27: 'es Spanish', 77: 'ms Malay', 127: 'uk Ukrainian',
    28: 'et Estonian', 78: 'mt Maltese', 128: 'ur Urdu',
    29: 'eu Basque', 79: 'my Burmese', 129: 'uz Uzbek',
    30: 'fa Persian', 80: 'na Nauru', 130: 'vi Vietnamese',
    31: 'fi Finnish', 81: 'ne Nepali', 131: 'vo Volapuk',
    32: 'fj Fiji', 82: 'nl Dutch', 132: 'wo Wolof',
    33: 'fo Faeroese', 83: 'no Norwegian', 133: 'xh Xhosa',
    34: 'fr French', 84: 'oc Occitan', 134: 'yo Yoruba',
    35: 'fy Frisian', 85: 'om (Afan) Oromo', 135: 'zh Chinese',
    36: 'ga Irish', 86: 'or Oriya', 136: 'zu Zulu',
    37: 'gd Scots Gaelic', 87: 'pa Punjabi',
    38: 'gl Galician', 88: 'pl Polish',
    39: 'gn Guarani', 89: 'ps Pashto, Pushto',
    40: 'gu Gujarati', 90: 'pt Portuguese',
    41: 'ha Hausa', 91: 'qu Quechua',
    42: 'hi Hindi', 92: 'rm Rhaeto-Romance',
    43: 'hr Croatian', 93: 'rn Kirundi',
    44: 'hu Hungarian', 94: 'ro Romanian',
    45: 'hy Armenian', 95: 'ru Russian',
    46: 'ia Interlingua', 96: 'rw Kinyarwanda',
    47: 'ie Interlingue', 97: 'sa Sanskrit',
    48: 'ik Inupiak', 98: 'sd Sindhi',
    49: 'in Indonesian', 99: 'sg Sangro',
    50: 'is Icelandic', 100: 'sh Serbo-Croatian',
}

# TODO: Copy from IPMI specification
ENTITY_ID = {
}
