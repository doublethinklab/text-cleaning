

class Error(Exception):
    pass


class UnsupportedGenre(Error):

    def __init__(self, genre: str):
        self.genre = genre


class UnsupportedLanguage(Error):

    def __init__(self, language: str):
        self.language = language
