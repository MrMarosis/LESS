from parse_evaluation_logic import parse_to_rpn,\
    evaluete_expresion,validate_expresion
import unittest


class TestPEL(unittest.TestCase):

    def test_parse_to_rpn(self):
        self.assertEqual(parse_to_rpn(['a', '&', 'b', '|', 'c']),
                         ['a', 'b', '&', 'c', '|'])

        self.assertEqual(parse_to_rpn('q>(~(p|q)&(p&r))|(q|r)'),
                         ['q', 'p', 'q', '|', '~', 'p', 'r', '&',
                          '&', '>', 'q', 'r', '|', '|'])

        self.assertEqual(parse_to_rpn('~~a'), ['a', '~', '~'])

        self.assertEqual(parse_to_rpn('a&b|(a>b)|~k=1'),
                         ['a', 'b', '&', 'a', 'b', '>', 'k', '~', '1', '=', '|', '|'])

        self.assertEqual(parse_to_rpn('~a|~b|d^f'),
                         ['a', '~', 'b', '~', 'd', 'f', '^', '|', '|'])

    def test_evaluete_expresion(self):
        self.assertEqual(evaluete_expresion(['1', '0', '&', '1', '|']), 1)

        self.assertEqual(evaluete_expresion(['1', '0', '>', ]), 0)

        self.assertEqual(evaluete_expresion(['1', '0', '^', '1', '&']), 1)

        self.assertEqual(evaluete_expresion(['1', '1', '&', '1', '1', '>',
                                             '1', '~', '1', '=', '|', '|']), 1)

        self.assertEqual(evaluete_expresion(['1', '0', '~', '&']), 1)

    def test_validate_expresion(self):
        self.assertEqual(validate_expresion('a&&a'), False)

        self.assertEqual(validate_expresion('~~~~~~~~~~a'), True)

        self.assertEqual(validate_expresion('a|b&c=(d>g)'), True)

        self.assertEqual(validate_expresion('a&1|1~'), False)

        self.assertEqual(validate_expresion('1|1'), True)


if __name__ == "__main__":
    unittest.main()
