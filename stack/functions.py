from class_Stack import Stack
from sequences_for_stack import dict_brackets


def find_coincidences(seq):
    stack = Stack()
    for bracket in seq:
        if bracket in dict_brackets.keys():
            stack.push(bracket)
        else:
            if stack.is_empty():
                return '''sequence isn't balanced'''
            else:
                if dict_brackets.get(stack.peek()) == bracket:
                    stack.pop()
                else:
                    return '''sequence isn't balanced'''
    if stack.is_empty():
        return 'sequence is balanced'
    else:
        return '''sequence isn't balanced'''
