import string

from zhon import hanzi

# unicode range for all languages: https://character-table.netlify.app/
# language specific chars
en_chars = string.ascii_lowercase + string.ascii_uppercase
zh_chars = r'\u4e00-\u9fff'
# https://stackoverflow.com/questions/19899554/unicode-range-for-japanese
ja_chars = r'\u3040-\u309f' + r'\u30a0-\u30ff' + r'\uff00-\uffef' \
           + r'\u4e00-\u9faf' + r'\u3005'
es_chars = 'áéíóúñüÁÉÍÓÚÑÜ'
# italian # https://character-table.netlify.app/italian/
it_chars = en_chars + 'ÀàÈèÉéÌìÒòÙù'
# french
fr_chars = en_chars +  r'\u00C0' + r'\u00C2' + r'\u00C6-\u00CB' + r'\u00CE-\u00CF' + \
    r'\u00D4' + r'\u00D9' + r'\u00DB-\u00DC' + r'\u00E0' + r'\u00E2' +   r'\u00E6-\u00EB' + r'\u00EE-\u00EF' + \
        r'\u00F4' + r'\u00F9' + r'\u00FB-\u00FC' + r'\u00FF' +  r'\u0152' + r'\u0153' + r'\u0178' + \
            r'\u02B3' + r'\u02E2' +  r'\u1D48-\u1D49'
# arabic
ar_chars =  r'\u0609'  +  r'\u061F' + r'\u0621-\u063A' + r'\u0611-\u064A' 


# digits
en_digits = string.digits
zh_digits = '０１２３４５６７８９'
ar_digits = r'\u0660-\u0669'
digits = en_digits + zh_digits + ar_digits


# punctuation
en_punct = string.punctuation
zh_punct = hanzi.punctuation
# ja_punct = r'\u3000-\u303f'  # already in hanzi.punctuation? # No
ja_punct = r'\u3001-\u3003' + r'\u3008-\u3011' + r'\u3014-\u3015' + r'\u301C'
es_punct = string.punctuation + '¡¿'
ar_punct = r'\u060C' + r'\u061B-\u061C' + r'\u061F' + r'\u064B-\u0652'
# NOTE: doesn't work to add ja_punct here, just grabs the chars in the above
punctuation = en_punct + zh_punct + es_punct + ja_punct + ar_punct


# contextual punctuations
word_start_punct = r'\[,."\'¡¿，。！？『｛（：；:'
word_end_punct = r'\],."\'!?，。！？』｝）：；;'


# sentence separators
sent_markers = hanzi.stops + '.?!'


# defines sets of acceptable characters
lang_to_chars = {
    'zh_cn': zh_chars + en_chars + punctuation + digits,
    'zh_tw': zh_chars + en_chars + punctuation + digits,
    'ja': ja_chars + en_chars + punctuation + digits,
    'en': en_chars + en_chars + punctuation + digits,
}
# defines sets of acceptable punctuation
lang_to_puncts = {
    'zh_cn': en_punct + zh_punct,
    'zh_tw': en_punct + zh_punct,
    'ja': en_punct + zh_punct,
    'en': en_punct,
}
