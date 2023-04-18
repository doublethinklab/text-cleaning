import string

from zhon import hanzi

# unicode range for all languages: https://character-table.netlify.app/
# language specific chars
en_chars = string.ascii_lowercase + string.ascii_uppercase
zh_chars = r'\u4e00-\u9fff'
# https://stackoverflow.com/questions/19899554/unicode-range-for-japanese
# ja_chars = r'\u3040-\u309f' + r'\u30a0-\u30ff' + r'\uff00-\uffef' \
#            + r'\u4e00-\u9faf' + r'\u3005'
# https://github.com/alvations/charguana
# https://github.com/ikegami-yukino/jaconv/blob/master/jaconv/conv_table.py
hiragana = 'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすず'\
            'せぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴ'\
            'ふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわ'\
            'をんーゎゐゑゕゖゔゝゞ'
katakana = 'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソ'\
            'ゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペ'\
            'ホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴヽヾ'
ja_chars = hiragana + katakana
# only add characters which differs from en_chars
# spanish
es_chars = 'áéíóúñüÁÉÍÓÚÑÜ'
# italian
it_chars = 'ÀàÈèÉéÌìÒòÙù'
# french
fr_chars = 'ÀÂÆÇÈÉÊËÎÏÔÙÛÜŸŒœàâæçèéêëîïôùûüÿ'
# arabic
# https://github.com/CAMeL-Lab/camel_tools/blob/master/camel_tools/utils/charsets.py
AR_LETTERS_CHARSET = '\u0621\u0622\u0623\u0624\u0625\u0626\u0627'\
                    '\u0628\u0629\u062a\u062b\u062c\u062d\u062e'\
                    '\u062f\u0630\u0631\u0632\u0633\u0634\u0635'\
                    '\u0636\u0637\u0638\u0639\u063a\u0640\u0641'\
                    '\u0642\u0643\u0644\u0645\u0646\u0647\u0648'\
                    '\u0649\u064a\u0671\u067e\u0686\u06a4\u06af'
AR_DIAC_CHARSET = '\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652\u0670\u0640'
ar_chars = AR_LETTERS_CHARSET + AR_DIAC_CHARSET 


# digits
en_digits = string.digits
zh_digits = '０１２３４５６７８９'
ar_digits = '٠١٢٣٤٥٦٧٨٩'
digits = en_digits + zh_digits + ar_digits


# punctuation
en_punct = string.punctuation
zh_punct = hanzi.punctuation
# ja_punct = r'\u3000-\u303f'  # already in hanzi.punctuation? Yes
es_punct = '¡¿'
ar_punct = '،؛؟' 
# NOTE: doesn't work to add ja_punct here, just grabs the chars in the above
punctuation = en_punct + zh_punct + es_punct + ar_punct


# contextual punctuations
word_start_punct = r'\[,."\'¡¿，。！？『｛（：；:、'
word_end_punct = r'\],."\'!?，。！？』｝）：；;、'


# sentence separators
sent_markers = hanzi.stops + '.?!'


# defines sets of acceptable characters
lang_to_chars = {
    # en chars included so proper names aren't broken
    'zh': zh_chars + en_chars + punctuation + digits,
    'ja': ja_chars + en_chars + punctuation + digits,
    # adding es chars to en so as not to break proper names
    'en': en_chars + es_chars + punctuation + digits,
    'es': es_chars + en_chars + punctuation + digits,
    'ar': ar_chars + en_chars + punctuation + digits,
    'fr': fr_chars + en_chars + punctuation + digits,
    'it': it_chars + en_chars + punctuation + digits,
}
# defines sets of acceptable punctuation
lang_to_puncts = {
    'zh': en_punct + zh_punct,
    'ja': en_punct + zh_punct,
    'en': en_punct,
    'es': en_punct + es_punct,
    'ar': en_punct + ar_punct,
    'fr': en_punct,
    'it': en_punct,
}
