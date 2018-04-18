from utilities import add_one_binary, compare_sequences, \
    replace_char, remove_list_duplicates

import unittest


class MyTestCase(unittest.TestCase):

    def test_add_one_binary(self):
        self.assertEqual(add_one_binary([0, 0, 0]), [0, 0, 1])

        self.assertEqual(add_one_binary([0]), [1])

        self.assertEqual(add_one_binary([1, 1, 0]), [1, 1, 1])

        #   Overflow is not supported
        self.assertEqual(add_one_binary([1, 1, 1]), None)

    def test_compare_sequences(self):
        self.assertEqual(compare_sequences([0, 1], [0, 1]), True)

        self.assertEqual(compare_sequences([0, 1], [0, 0]), False)

        self.assertEqual(compare_sequences(['-', 0], [0, '-']), False)

        #   There is no known variation of algorithm which requires it
        #   self.assertEqual(compare_sequences([0, 0], [0, 0, 0]), False)

    def test_replace_char(self):
        self.assertEqual(replace_char(['a', 'b', 'c'], 'a', 1),
                         [1, 'b', 'c'])

        self.assertEqual(replace_char(['~', 'a', '&', 'a'], 'a', 1),
                         ['~', 1, '&', 1])

        self.assertEqual(replace_char(['(', 'a', ')'], 'a', 0),
                         ['(', 0, ')'])

    def test_remove_list_duplicates(self):
        self.assertEqual(remove_list_duplicates([1, 1, 1, 1, 1]), [1])

        self.assertEqual(remove_list_duplicates([1, '1', 1]), [1, '1'])

        self.assertEqual(remove_list_duplicates([1, '1', 1]), [1, '1'])


if __name__ == '__main__':
    unittest.main()
