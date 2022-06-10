"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

https://leetcode.com/problems/min-stack/
"""


class MinStack1:
    """Approach 1: Stack of Value/ Minimum Pairs

    All operations are O(1) time complexity
    push() is O(n)
    """

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        O(n) space complexity
        """
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


class MinStack2:
    """Approach 2: Two Stacks

    We could instead have two Stackss inside our MinStack. The main Stack should keep
    track of the order numbers arrived (a standard Stack), and the second Stack should
    keep track of the current minimum


    Complexity:
        * Time complexity: All operations are O(1)
        * Space complexity: push() is O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


class MinStack3:
    """Approach 3: Two Stacks

    In the above approach, we pushed a new number onto the min-tracker Stack if, and
    only if, it was less than or equal to the current minimum.
    One downside of this solution is that if the same number is pushed repeatedly onto
    MinStack, and that number also happens to be the current minimum, there'll be a lot
    of needless repetition on the min-tracker Stack. Recall that we put this repetition
    in to prevent a bug from occurring (refer to Approach 2).


    Complexity:
        * Time complexity: All operations are O(1)
        * Space complexity: push() is O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        # We always put the number onto the main stack.
        self.stack.append(x)

        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])

        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self):
        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

        # And like before, pop the top of the main stack.
        self.stack.pop()

    def top(self):
        return self.stack[-1]


if __name__ == "__main__":
    minStack = MinStack1()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()  # return -3
    minStack.pop()
    minStack.top()  # return 0
    minStack.getMin()  # return -2
