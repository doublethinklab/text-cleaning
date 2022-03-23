import re

from text_cleaning import chars


either_slash = re.compile(r'(\s|^)[\w]+(?P<target>/)[\w]+([\s.,]|$)')
punctuation = re.compile(r'[%s]' % re.escape(chars.punctuation))
mention = re.compile(r'([\s%s]|^)(?P<target>@[\w]+)([\s%s]|$)' \
          % (re.escape(chars.punctuation), re.escape(chars.punctuation)))
html = re.compile(r'<.*?>')
