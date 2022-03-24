import re
from typing import List, Union

from text_cleaning import chars


either_slash = re.compile(r'(\s|^)[\w]+(?P<target>/)[\w]+([\s.,]|$)')
punctuation = re.compile(r'[%s]' % re.escape(chars.punctuation))
mention = re.compile(r'([\s%s]|^)(?P<target>@[\w]+)([\s%s]|$)' \
          % (re.escape(chars.punctuation), re.escape(chars.punctuation)))
html = re.compile(r'<.*?>')
hashtag = re.compile(r'([\s%s]|^)(?P<target>#[\w\d]+#?)([\s%s]|$)'
                     % (re.escape(chars.punctuation),
                        re.escape(chars.punctuation)))


def extract_matches(text: str, regexp: Union[str, re.Pattern]) -> List[str]:
    return [m.groupdict()['target'] for m in re.finditer(regexp, text)]


def matches_target(token: str, regexp: Union[str, re.Pattern]) -> bool:
    return re.match(regexp, token) is not None
