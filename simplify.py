from parse_evaluation_logic import parse_to_rpn, evaluete_expresion, \
    __operators, validate_expresion
from utilities import replace_char, add_one_binary, compare_sequences, \
    remove_list_duplicates
import sys


def get_true_value_sequences(rpn_expression, variables):
    """
    Returns list of value sequences for whom given expression evaluates to true.

    :param rpn_expression: String rpn expression
    :param variables: Set of variables
    :return: List of lists of 0 and 1.
    """
    binary_num = [0 for i in variables]
    res = []
    for i in range(0, 2 ** len(variables)):
        tmp_rpn = rpn_expression[:]
        for variable, value in zip(variables, binary_num):
            tmp_rpn = replace_char(tmp_rpn, variable, value)
        if evaluete_expresion(tmp_rpn) == True:
            res.append(binary_num[:])
        binary_num = add_one_binary(binary_num)
    return res


def gen_ancestors_seqences_num(sequences):
    """
    For each sequence returns order numbers of starting 
    sequences used to create given simplified sequence.

    Mechanism: generate parent expression and turn it into
    its order number.
    
    :param sequences: list of variable sequences expressions
    :return: List of order numbers of parent sequences for each sequence
    """
    order_numbers = []
    for sequence in sequences:
        tmp_sequence = [0 for i in sequence]
        group_pgroups = []
        for i in range(2 ** len(sequence)):
            if compare_sequences(sequence, tmp_sequence):
                group_pgroups.append(int(''.join(map(str, tmp_sequence)), 2))
            tmp_sequence = add_one_binary(tmp_sequence)
        order_numbers.append(group_pgroups)
    return order_numbers


def find_prime(groups):
    """
    Returns prime sequences.
    
    :param groups: List of sublist, each sublist has given number of one's.
    :return: Prime sequences.
    """
    groups = remove_list_duplicates(groups)
    groups_numbers = \
        gen_ancestors_seqences_num([subgroup for subgroup in groups if subgroup])
    primes = []
    for group, number_group in zip(groups, groups_numbers):
        for num in number_group:
            if ([item for slist in groups_numbers for item in slist].count(num) 
                    == 1 and group not in primes):
                primes.append(group)
    return primes


def group_expressions(sequences, variable_number):
    """
    Returns grouped sequences, groups according to number of one's.

    :param sequences: List of variable sequences 
    :param variable_number: Number of variables
    :return: List with sublist in which sequences have same numbers of one's.
    """
    grouped_expressions = [[] for i in range(variable_number + 1)]
    for group in sequences:
        grouped_expressions[group.count(1)].append(group)
    return grouped_expressions


def simplify_sequences(sequence_one, sequence_two):
    """Return simplified sequence or an empty one if not possible to create one"""
    diffrences = 0
    new_merged_component = []
    for token_one, token_two in zip(sequence_one, sequence_two):
        if (token_one != token_two):
            new_merged_component.append('-')
            diffrences += 1
        else:
            new_merged_component.append(token_one)
    if diffrences == 1:
        return new_merged_component
    else:
        return []


def quine_mccluskey(sequences, prime_sequences, variable_number):
    """
    Implementation of Quine-McCluskey method.

    :param sequences: List of sequences for whom given expression is true.
    :param prime_sequences: Sequences which can no longer be simplified.
    :param variable_number: Number of variables.
    :return: Simplified expression.
    """
    assigned_groups = group_expressions(sequences, variable_number)
    merged_groups = []
    not_prime_sq = []
    for group_index in range(len(assigned_groups) - 1):
        for sequence_one in assigned_groups[group_index]:
            for sequence_two in assigned_groups[group_index + 1]:
                new_component = simplify_sequences(sequence_one, sequence_two)
                if not new_component:
                    continue
                else:
                    merged_groups.append(new_component)
                    if sequence_one not in not_prime_sq:
                        not_prime_sq.append(sequence_one)
                    if sequence_two not in not_prime_sq:
                        not_prime_sq.append(sequence_two)
    prime_sequences.extend([sq for sq in sequences if sq not in not_prime_sq])
    if merged_groups == []:
        return find_prime(prime_sequences)
    else:
        return quine_mccluskey(merged_groups, prime_sequences, variable_number)


def gen_result_string(groups, vars):
    """ Creates a string representing result of quince-McCluskey method. """
    result = []
    for element in groups:
        for var, token in zip(vars, element):
            if (token == '-'):
                continue
            elif token == 0:
                result.extend(['(', '~', var, ')', '&'])
            else:
                result.extend([var, '&'])
        result = result[:-1]
        result.extend(['|'])
    result = result[:-1]
    return result if result != [] else '1'


def main():
    if(len(sys.argv)==1):
        print("No argument provided")
    else:
        #print(sys.argv)
        args = [char for arg in sys.argv[1:] for char in arg]
        #print(args)
        if validate_expresion(args):
            rpn = parse_to_rpn(args)
            #print(rpn)

            vars = sorted(set(list(filter(lambda x: x not in __operators and
                                         x not in ('1', '0'), rpn))))
            true_sequences = get_true_value_sequences(rpn,vars)
            #print(true_sequences)

            result = quine_mccluskey(true_sequences,[],len(vars))
            #print(result)

            simplified_expression = gen_result_string(result,vars)
            #print(simplified_expression)
        else:
            #print("Wrong input acceptable operators: ",__operators,
                  "\nacceptable values: ",__operators)


if __name__ == '__main__':
    main()
