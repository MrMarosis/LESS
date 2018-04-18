import string

"""
    Following module is 100% replaceable, feel free to modify it as you wish. 
"""

__variables = string.ascii_lowercase+'01'
__operators = {'&': 3, '>': 3, '^': 2, '=': 2, '|': 1, '(':0,')':None,'~': 4}

def parse_to_rpn(string):
    """ Returns expression in rpn. """
    stack=[]
    rpn=[]
    for token in string:
        if token not in __operators.keys():
            rpn.append(token)
        elif token == ')':
            x = stack.pop()
            while(x!='('):
                rpn.append(x)
                x = stack.pop()
        elif __operators.get(token)==0:
            stack.append(token)
        elif stack and __operators.get(token) > __operators.get(stack[-1]):
            stack.append(token)
        else:
            while(stack and __operators.get(token) < __operators.get(stack[-1])):
                x = stack.pop()
                if x != '(':
                    rpn.append(x)
            stack.append(token)
    while stack:
        rpn.append(stack.pop())
    return rpn


def evaluete_expresion(rpn):
    """ Returns result of evaluating expression. """
    stack=[]
    for char in rpn:
        if(char not in __operators):
            stack.append(char)
        elif char is '~':
            stack.append(not bool(int(stack.pop())))
        else:
            x = bool(int(stack.pop()))
            y = bool(int(stack.pop()))
            if char is '&':
                stack.append(x and y)
            elif char is '|':
                stack.append(x or y)
            elif char is '^':
                stack.append(x != y)
            elif char is '=':
                stack.append(x == y)
            elif char is '>':
                stack.append(x or not y)
    return stack.pop()

def validate_expresion(expr):
    """ Returns True if given input is correct. """
    state = True
    par_count = 0
    for char in expr:
        if char == " ":
            continue
        if char == '~':
            state=True
            continue
        if state:
            if char in __variables: state = False
            elif char == "(":
                par_count += 1
            else:
                return False
        else:
            if char == ')': par_count -= 1
            elif char in list(__operators.keys()): state = True
            else: return False
        if par_count < 0: return False
    return par_count == 0 and not state
