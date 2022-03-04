import re 
from text_cleaning.functions.base import CleanText

class FrenchDeAbbreviation(CleanText):

    def clean(self, text:str, **kwargs) -> str:
        text = re.sub('d\’', ' ', text)
        text = re.sub('l\’', ' ', text)
        text = re.sub('L\’', ' ', text)
        text = re.sub('n\’a', ' ', text)
        return text