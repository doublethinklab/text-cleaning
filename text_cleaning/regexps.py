import re

from text_cleaning import chars


either_slash = r'(\s|^)[\w]+(?P<target>/)[\w]+([\s.,]|$)'
punctuation = r'[%s]' % re.escape(chars.punctuation)
mention = r'([\s%s]|^)(?P<target>@[\w]+)([\s%s]|$)' \
          % (re.escape(chars.punctuation), re.escape(chars.punctuation))
