import re
from typing import List

from text_cleaning import chars, languages as lang, replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceGarbage(ReplaceInText):
    """We rule *in* valid characters to avoid enumerating all garbage.

    This is the set of English, Chinese, and Japanese characters, including
    their punctuation marks, and digits.
    """

    def __init__(self,
                 replacement: str = replacements.JUNK,
                 languages: List[str] = lang.supported_languages):
        super().__init__(replacement=replacement)
        self.languages = languages
        self.regex = self.build_regex(languages)

    @staticmethod
    def build_regex(languages: List[str]):
        regex = '[^'
        if lang.en_us in languages:
            regex += chars.en_chars
        if lang.zh_cn in languages or lang.zh_tw in languages:
            regex += chars.zh_chars
        if lang.ja_jp in languages:
            regex += chars.ja_chars
        if lang.es_es in languages:
            regex += chars.es_chars
            regex += chars.en_chars
        regex += chars.punctuation
        regex += chars.digits
        regex += '\s+]'
        return regex

    def clean(self, text: str, **kwargs) -> str:
        return re.sub(self.regex, self.replacement, text)


class RemoveGarbage(ReplaceGarbage):

    def __init__(self, languages: List[str] = lang.supported_languages):
        super().__init__(replacement='', languages=languages)
