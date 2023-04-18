import re
from typing import List

from text_cleaning import chars, languages as lang, replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceGarbage(ReplaceInText):
    """We rule *in* valid characters to avoid enumerating all garbage.

    This is the set of English, Chinese, and Japanese characters, including
    their punctuation marks, and digits.
    """

    def __init__(
            self,
            replacement: str = replacements.JUNK,
            languages: List[str] = lang.supported_languages
    ):
        assert all(l in lang.supported_languages for l in languages)
        super().__init__(replacement=replacement)
        self.languages = languages
        self.regex = self.build_regex(languages)

    @staticmethod
    def build_regex(languages: List[str]):
        regex = '[^'
        for language in languages:
            regex += chars.lang_to_chars[language]
        regex += re.escape(chars.punctuation)
        regex += chars.digits
        regex += '\s+]'
        return re.compile(regex)

    def clean(self, text: str, **kwargs) -> str:
        return re.sub(self.regex, self.replacement, text)


class RemoveGarbage(ReplaceGarbage):

    def __init__(
            self,
            languages: List[str] = lang.supported_languages
    ):
        assert all(l in lang.supported_languages for l in languages)
        super().__init__(replacement='', languages=languages)
