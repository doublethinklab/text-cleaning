import logging
import sys
import unittest

from text_cleaning.functions.text.standardization import StandardizeText


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.propagate = False
    return logger


class TestStandardizeText(unittest.TestCase):

    def test_case_1(self):
        standardize = StandardizeText(
            rules={
                'USA': ['U.S.A', 'U.S.', 'America'],
            })
        text = 'The U.S. government serves America, and everyone in the U.S.A.'
        result = standardize(text)
        expected = 'The USA government serves USA, and everyone in the USA.'
        self.assertEqual(expected, result)

    def test_debugging(self):
        standardize = StandardizeText(
            rules={
                'USA': ['U.S.A', 'U.S.', 'America'],
            },
            logger=get_logger(),
            debug=True)
        text = 'The U.S. government serves America, and everyone in the U.S.A.'
        result = standardize(text)
        expected = 'The USA government serves USA, and everyone in the USA.'
        self.assertEqual(expected, result)
