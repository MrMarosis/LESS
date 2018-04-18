from simplify import find_prime, \
    get_true_value_sequences, gen_ancestors_seqences_num, simplify_sequences, \
    group_expressions

import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.__operators = {'&': 3, '>': 3, '^': 2, '=': 2, '|': 1, '(': 0,
                            ')': None, '~': 4}

    def test_get_true_value_sequences(self):
        rpn = ['a', 'b', '&']

        variables = sorted(set(list(filter(lambda x: x not in self.__operators and
                                                     x not in ('1', '0'), rpn))))

        self.assertEqual(get_true_value_sequences(rpn, variables), [[1, 1]])

        rpn = ['q', 'p', 'q', '|', '~', 'p', 'r',
               '&', '&', '>', 'q', 'r', '|', '|']

        variables = sorted(set(list(filter(lambda x: x not in self.__operators and
                                                     x not in ('1', '0'), rpn))))

        self.assertEqual(get_true_value_sequences(rpn, variables), [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
                                                                    [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])

        rpn = ['a', 'b', '&', 'a', 'b', '>', 'k', '~', '1', '=', '|', '|']

        variables = sorted(set(list(filter(lambda x: x not in self.__operators and
                                                     x not in ('1', '0'), rpn))))

        self.assertEqual(get_true_value_sequences(rpn, variables), [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
                                                                    [1, 0, 0], [1, 1, 0], [1, 1, 1]])

    def test_gen_ancestors_seqences_num(self):
        self.assertEquals(gen_ancestors_seqences_num([[1, '-']]), [[2, 3]])

        self.assertEquals(gen_ancestors_seqences_num([[1, 1], ['-', '-']]),
                          [[3], [0, 1, 2, 3]])

        self.assertEquals(gen_ancestors_seqences_num([['-']]),
                          [[0, 1]])

    def test_group_expressions(self):
        self.assertEquals(group_expressions([[1, 1], [0, 1], [0,0]], 2),
                          [[[0, 0]], [[0, 1]], [[1, 1]]])
        self.assertEquals(group_expressions([[1, 0], [0, 1], [0, 0]], 2),
                          [[[0, 0]], [[1, 0], [0, 1]], []])
        self.assertEquals(group_expressions([[1], [1], [1]], 1),
                          [[], [[1], [1], [1]]])

    def test_find_prime(self):
        self.assertEquals(find_prime([[0,1],[1,0]]),[[0, 1], [1, 0]])

        self.assertEquals(find_prime([['-', 1],[0,1]]), [['-', 1]])

        self.assertEquals(find_prime([['-', 1, '-']]), [['-', 1, '-']])

    def test_simplify_sequences(self):
        self.assertEquals(simplify_sequences([1,0,0],[1,1,0]),[1,'-',0])

        self.assertEquals(simplify_sequences([1, '-', 0], [1, 1, 0]), [1, '-', 0])

        self.assertEquals(simplify_sequences([1, 0, 0], [1, 1, 1]), [])



if __name__ == '__main__':
    unittest.main()
