""" A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
"""
class Stack(object):
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        """ Push an element to the top of the stack."""
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        """ Peek at the top-most element of the stack."""
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def size(self):
        """ Return the size of the stack."""
        return len(self.stack)

if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print('Stack demonstration:\n')
    print('Initial stack: ' + str(stack))
    print('pop(): ' + str(stack.pop()))
    print('After pop(), the stack is now: ' + str(stack))
    print('peek(): ' + str(stack.peek()))
    stack.push(100)
    print('After push(100), the stack is now: ' + str(stack))
    print('is_empty(): ' + str(stack.is_empty()))
    print('size(): ' + str(stack.size()))


"""
Output:
Stack demonstration:
Initial stack: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pop(): 9
After pop(), the stack is now: [0, 1, 2, 3, 4, 5, 6, 7, 8]
peek(): 8
After push(100), the stack is now: [0, 1, 2, 3, 4, 5, 6, 7, 8, 100]
is_empty(): False
size(): 10
"""