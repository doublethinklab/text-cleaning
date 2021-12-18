from typing import Dict, List, Optional

from text_cleaning import chars
from text_cleaning.functions.base import CleanText


class StandardizeText(CleanText):

    def __init__(self, rules: Optional[Dict[str, List[str]]] = None):
        # rules is a Dict like {replacement: [regexs]},
        # e.g. {'usa': ['U.S.', 'U.S.A.', ...]}
        # designed to go BEFORE lowercasing of the text,
        # so the replacement will always be lowercased anyway if you lowercase,
        # also note the order matters - e.g. if you first replace `Trump`, but
        # then try to replace `Donald Trump`, obviously you have already broken
        # the latter instances.
        self.rules = rules

    @staticmethod
    def _get_regex(original: str) -> str:
        return r'([\s%s]|^)+' \
               r'(?P<target>%s)' \
               r'([\s%s]|$)+' \
               % (chars.word_start_punct, original, chars.word_end_punct)

    def clean(self, text: str, **kwargs) -> str:
        if self.rules is None:
            return text
        for replacement, originals in self.rules.items():
            for original in originals:
                regex = self._get_regex(original)
                text = self.replace_all(regex, text, replacement)
        return text
