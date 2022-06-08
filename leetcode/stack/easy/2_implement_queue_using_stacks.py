"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

https://leetcode.com/problems/implement-queue-using-stacks/
"""


class MyQueue1:
    """Approach 1

    push O(n)
    pop O(1)
    """

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        # Move all elements from the first stack to the second stack
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        # Push item onto first stack
        self.stack_1.append(x)

        # Move all elements back to the first stack from the second stack
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def pop(self):
        return self.stack_1.pop()

    def peek(self):
        return self.stack_1[-1]

    def empty(self):
        return not self.stack_1


class MyQueue2:
    """Approach 2

        push O(1)
        pop amortized O(1) | worst case O(n)

    Amortized analysis gives the average performance (over time) of each operation in
    the worst case. The basic idea is that a worst case operation can alter the state in
    such a way that the worst case cannot occur again for a long time, thus amortizing
    its cost
    """

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        self.stack_1.append(x)

    def pop(self):
        self.peek()
        return self.stack_2.pop()

    def peek(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2[-1]

    def empty(self):
        return not self.stack_1 and not self.stack_2


if __name__ == "__main__":
    myQueue = MyQueue1()
    myQueue.push(1)  # queue is: [1]
    myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek()  # return 1
    myQueue.pop()  # return 1, queue is [2]
    myQueue.empty()  # return false
