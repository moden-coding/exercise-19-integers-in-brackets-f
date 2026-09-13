#!/usr/bin/env python3
"""Tests for the Integers in Brackets assignment."""

import unittest

from src.integers_in_brackets import integers_in_brackets


class TestIntegersInBrackets(unittest.TestCase):
    """integers_in_brackets(s) -> list of the ints found inside [brackets]."""

    def test_worked_example(self):
        s = "  afd [asd] [12 ] [a34]  [\t -43 ]tt [+12]xxx"
        result = integers_in_brackets(s)
        self.assertIsInstance(
            result,
            list,
            msg="integers_in_brackets should return a list. Got %s."
            % (type(result),),
        )
        self.assertEqual(
            result,
            [12, -43, 12],
            msg="Incorrect result for string %r! Expected [12, -43, 12]: "
            "'[asd]' and '[a34]' contain no plain integer and must be "
            "skipped." % (s,),
        )

    def test_multi_sign_tokens_are_rejected(self):
        s = "  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"
        result = integers_in_brackets(s)
        self.assertIsInstance(
            result,
            list,
            msg="integers_in_brackets should return a list. Got %s."
            % (type(result),),
        )
        self.assertEqual(
            result,
            [47, 12],
            msg="Incorrect result for string %r! Expected [47, 12]: "
            "'[128+]' (trailing sign) and '[ +-43 ]' (two signs) are not "
            "valid integers and must be skipped." % (s,),
        )

    def test_empty_string_gives_an_empty_list(self):
        result = integers_in_brackets("")
        self.assertIsInstance(
            result,
            list,
            msg="integers_in_brackets should return a list. Got %s."
            % (type(result),),
        )
        self.assertEqual(
            result,
            [],
            msg="Incorrect result for an empty string!",
        )


if __name__ == '__main__':
    unittest.main()
