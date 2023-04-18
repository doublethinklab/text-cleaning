import unittest

from text_cleaning.pipelines.facebook.en \
    import CleanEnglishFacebookText, CleanEnglishFacebookTokens


class TestCleanEnglishFacebookText(unittest.TestCase):

    def test_case_1(self):
        text = """Live: Oriental white storks enter peak incubation period at Yellow River Delta National Nature Reserve
The Oriental white stork, a migratory bird species under China's first-class nationally protection, has been listed as an Endangered Species in the International Union for Conservation of Nature (IUCN) Red List of Threatened Species. As the conservation work progress, artificial bird nests have been built at the Yellow River Delta National Nature Reserve in Dongying, east China's Shandong Province. Oriental white storks there are enjoying their new nests and their nestlings are embracing the world. #YellowRiverAdventures"""
        clean = CleanEnglishFacebookText()
        cleaned = clean(text)
        expected = """live: oriental white storks enter peak incubation period at yellow river delta national nature reserve. the oriental white stork, a migratory bird species under china first-class nationally protection, has been listed as an endangered species in the international union for conservation of nature (iucn) red list of threatened species. as the conservation work progress, artificial bird nests have been built at the yellow river delta national nature reserve in dongying, east china shandong province. oriental white storks there are enjoying their new nests and their nestlings are embracing the world. #yellowriveradventures"""
        self.assertEqual(expected, cleaned)


class TestCleanEnglishFacebookTokens(unittest.TestCase):

    def test_case_1(self):
        tokens = [
            'live:', 'oriental', 'white', 'storks', 'enter', 'peak',
            'incubation', 'period', 'at', 'yellow', 'river', 'delta',
            'national', 'nature', 'reserve', '.', 'the', 'oriental', 'white',
            'stork,', 'a', 'migratory', 'bird', 'species', 'under', 'china',
            'first-class', 'nationally', 'protection,', 'has', 'been',
            'listed', 'as', 'an', 'endangered', 'species', 'in', 'the',
            'international', 'union', 'for', 'conservation', 'of', 'nature',
            '(iucn)', 'red', 'list', 'of', 'threatened', 'species.', 'as',
            'the', 'conservation', 'work', 'progress,', 'artificial', 'bird',
            'nests', 'have', 'been', 'built', 'at', 'the', 'yellow', 'river',
            'delta', 'national', 'nature', 'reserve', 'in', 'dongying,',
            'east', 'china', 'shandong', 'province.', 'oriental', 'white',
            'storks', 'there', 'are', 'enjoying', 'their', 'new', 'nests',
            'and', 'their', 'nestlings', 'are', 'embracing', 'the', 'world.',
            '#yellowriveradventures']
        clean = CleanEnglishFacebookTokens()
        cleaned = clean(tokens)
        expected = [
            'live', 'oriental', 'white', 'storks', 'enter', 'peak',
            'incubation', 'period', 'at', 'yellow', 'river', 'delta',
            'national', 'nature', 'reserve', 'the', 'oriental', 'white',
            'stork', 'a', 'migratory', 'bird', 'species', 'under', 'china',
            'first', 'class', 'nationally', 'protection', 'has', 'been',
            'listed', 'as', 'an', 'endangered', 'species', 'in', 'the',
            'international', 'union', 'for', 'conservation', 'of', 'nature',
            'iucn', 'red', 'list', 'of', 'threatened', 'species', 'as', 'the',
            'conservation', 'work', 'progress', 'artificial', 'bird', 'nests',
            'have', 'been', 'built', 'at', 'the', 'yellow', 'river', 'delta',
            'national', 'nature', 'reserve', 'in', 'dongying', 'east', 'china',
            'shandong', 'province', 'oriental', 'white', 'storks', 'there',
            'are', 'enjoying', 'their', 'new', 'nests', 'and', 'their',
            'nestlings', 'are', 'embracing', 'the', 'world',
            'yellowriveradventures']
        self.assertEqual(expected, cleaned)
