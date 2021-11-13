import string

from zhon import hanzi


# replacement chars
URL = 'URL'
NUM = 'NUM'
JUNK = 'JUNK'


# punctuation
en_punct = string.punctuation
zh_punct = hanzi.punctuation
ja_punct = r'\u3000-\u303f'
es_punct = string.punctuation + '¡¿'
punctuation = ''.join(list(set(en_punct + zh_punct + ja_punct + es_punct)))


# language specific chars
en_chars = string.ascii_lowercase + string.ascii_uppercase
zh_chars = r'\u4e00-\u9fff'
# https://stackoverflow.com/questions/19899554/unicode-range-for-japanese
ja_chars = r'\u3040-\u309f' + r'\u30a0-\u30ff' + r'\uff00-\uffef' \
           + r'\u4e00-\u9faf'
es_chars = 'áéíóúñüÁÉÍÓÚÑÜ'


# digits
en_digits = string.digits
zh_digits = '０１２３４５６７８９'
digits = en_digits + zh_digits


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
    'ja': en_punct + ja_punct,
    'en': en_punct,
}
