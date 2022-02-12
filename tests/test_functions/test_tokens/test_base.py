import unittest

from data_structures.nlp import Token

from text_cleaning.functions.base import CleanTokens


class TestSplitTokensOnSpace(unittest.TestCase):

    def test_split_works_for_non_entities(self):
        tokens = [
            Token('I'), Token('do not'), Token('know'),
        ]
        split = CleanTokens.split_on_space(tokens)
        expected = [
            Token('I'), Token('do'), Token('not'), Token('know'),
        ]
        self.assertEqual(expected, split)

    def test_split_ignores_entities(self):
        tokens = [
            Token('Lebron James', is_entity=True, entity_type='PER'),
            Token('licks'),
            Token('Xi', is_entity=True, entity_type='ANIMAL'),
        ]
        split = CleanTokens.split_on_space(tokens)
        self.assertEqual(tokens, split)
