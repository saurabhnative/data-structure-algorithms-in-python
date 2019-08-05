"""
Check for balanced parentheses in an expression
Given an expression string exp , write a program to examine
whether the pairs and the orders of ”(“,”)” are correct in exp.
"""

from stack import Stack


def balanced_parentheses(parentheses):
    """ Use a stack to check if a string of parentheses is balanced."""
    stack = Stack()
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parentheses)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))