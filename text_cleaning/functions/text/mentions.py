from text_cleaning import chars, replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceMentions(ReplaceInText):

    def __init__(self, replacement: str = replacements.MENTION):
        super().__init__(replacement=replacement)
        self.regex = r'[\s%s](?P<target>@[\w]+)([\s%s]|$)' \
                     % (chars.punctuation, chars.punctuation)

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(self.regex, self.replacement, text)

