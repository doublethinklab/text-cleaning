from typing import Dict, List, Optional

from text_cleaning import chars
from text_cleaning.functions.base import CleanText


class StandardizeText(CleanText):

    @staticmethod
    def _get_regex(original: str) -> str:
        return r'([\s%s]|^)+' \
               r'(?P<target>%s)' \
               r'([\s%s-]|$)+' \
               % (chars.word_start_punct, original, chars.word_end_punct)

    def clean(
            self,
            text: str,
            standardization_rules: Optional[Dict[str, List[str]]] = None,
            **kwargs
    ) -> str:
        # rules is a Dict like {replacement: [regexs]},
        # e.g. {'usa': ['U.S.', 'U.S.A.', ...]}
        # designed to go BEFORE lowercasing of the text,
        # so the replacement will always be lowercased anyway if you lowercase,
        # also note the order matters - e.g. if you first replace `Trump`, but
        # then try to replace `Donald Trump`, obviously you have already broken
        # the latter instances.
        if standardization_rules is None:
            return text
        for replacement, originals in standardization_rules.items():
            for original in originals:
                regex = self._get_regex(original)
                if self.debug:
                    self.logger.debug(f'Standardizing {replacement}, from: %s'
                                      % ', '.join(originals))
                    self.logger.debug(f'Regex: {regex}')
                text = self.replace_all(regex, text, replacement)
                if self.debug:
                    self.logger.debug(f'Result: {text}')
        return text
