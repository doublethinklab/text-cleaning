import re
from typing import List, Union

from text_cleaning import chars


# TODO: proper way to deal with this pre-compiling
#  we clearly need the strings as well, as e.g. when removing # from punctuation
#  but pre-compiling is a speed advantage
#  so maybe the cleaning functions that use them should be responsible for that


# raw strings
r_punctuation = r'[%s]' % re.escape(chars.punctuation)
# https://stackoverflow.com/questions/839994/extracting-a-url-in-python
r_url = '(?P<target>((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]' \
        '{2,6})|(?:' \
        '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]' \
        '|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|' \
        '(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]' \
        '{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:' \
        '[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]' \
        '{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}' \
        '(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]' \
        '{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]' \
        '{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:' \
        '(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|' \
        '(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:' \
        '(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|' \
        '(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6' \
        '[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]' \
        '*)*/?))'


# pre-compiled
either_slash = re.compile(r'(\s|^)[\w]+(?P<target>/)[\w]+([\s.,]|$)')
punctuation = re.compile(r'[%s]' % re.escape(chars.punctuation))
mention = re.compile(r'([\s%s]|^)(?P<target>@[\w]+)([\s%s]|$)' \
          % (re.escape(chars.punctuation), re.escape(chars.punctuation)))
html = re.compile(r'<.*?>')
hashtag = re.compile(r'([\s%s]|^)(?P<target>#[\w\d]+#?)([\s%s]|$)'
                     % (re.escape(chars.punctuation),
                        re.escape(chars.punctuation)))
url = re.compile(r_url)


def extract_matches(text: str, regexp: Union[str, re.Pattern]) -> List[str]:
    return [m.groupdict()['target'] for m in re.finditer(regexp, text)]


def matches_target(token: str, regexp: Union[str, re.Pattern]) -> bool:
    return re.match(regexp, token) is not None
