from text_cleaning.functions.text.apostrophe_s import \
    RemoveTrailingApostropheS
from text_cleaning.functions.text.either_slash import \
    ReplaceEitherSlashWithSpace
from text_cleaning.functions.text.garbage import \
    RemoveGarbage, \
    ReplaceGarbage
from text_cleaning.functions.text.hashtags import \
    RemoveHashtags
from text_cleaning.functions.text.html import \
    RemoveHtml
from text_cleaning.functions.text.lowercase import \
    LowerCase
from text_cleaning.functions.text.mentions import \
    ReplaceMentions
from text_cleaning.functions.text.numbers import \
    RemoveNumbers, \
    ReplaceNumbers
from text_cleaning.functions.text.punctuation import \
    RemovePunctuation, \
    ReplacePunctuation
from text_cleaning.functions.text.standardization import \
    StandardizeText
from text_cleaning.functions.text.trad2simp import \
    TraditionalToSimplified
from text_cleaning.functions.text.whitespace import \
    NormalizeWhitespace, \
    SingleNewlineToSpace
from text_cleaning.functions.text.halfwidth import \
    NormalizeTextWidth
from text_cleaning.functions.text.de_abbreviation import \
    FrenchDeAbbreviation
from text_cleaning.functions.text.urls import \
    RemoveUrls, ReplaceUrls
