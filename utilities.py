def add_one_binary(list):
    """ Increments binary number written in list. """
    for i in range(len(list)-1,-1,-1):
        if list[i]==0:
            list[i]=1
            return list
        else:
            list[i]=0


def compare_sequences(num_one,num_two):
    """ Compares sequences. """
    for token_one, token_two in zip(num_one,num_two):
        if(token_one == '-' or token_one==token_two):
            continue
        else:
            return False
    return True


def replace_char(_list,char,value):
    """ Replaces a char in list. """
    return list(map(lambda c: value if c is char else c, _list))


def remove_list_duplicates(list):
    """ Return duplicate free list. """
    new_list = []
    for token in list:
        if token not in new_list:
            new_list.append(token)
    return new_list