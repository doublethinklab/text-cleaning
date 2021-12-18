from text_cleaning import chars


either_slash = r'(\s|^)[\w]+(?P<target>/)[\w]+([\s.,]|$)'
punctuation = r'[%s]' % chars.punctuation
