from textacy.preprocessing import normalize

from text_cleaning import languages
from text_cleaning.functions.base import CleanText, ReplaceInText


class NormalizeWhitespace(CleanText):
    """Implements normalization as in textacy:

    Replace all contiguous zero-width spaces with an empty string,
    line-breaking spaces with a single newline, and non-breaking spaces with a
    single space, then strip any leading/trailing whitespace."""

    def clean(self, text: str, **kwargs) -> str:
        return normalize.whitespace(text)


class SingleNewlineToSpace(ReplaceInText):

    def __init__(self, logger=None, debug: bool = False):
        super().__init__(replacement=' ', logger=logger, debug=debug)
        self.regex = r'[^\n]+(?P<target>\n)[^\n]'

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(self.regex, text, self.replacement)


class SingleNewlineToPeriod(ReplaceInText):

    def __init__(self, language: str, logger=None, debug: bool = False):
        super().__init__(
            replacement=self.get_period(language),
            logger=logger,
            debug=debug)
        self.regex = r'[^\n]+(?P<target>\n)[^\n]'

    @staticmethod
    def get_period(language: str) -> str:
        if language == languages.en:
            return '. '
        elif language == languages.zh:
            return '。'
        else:
            raise ValueError(language)

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(self.regex, text, self.replacement)
