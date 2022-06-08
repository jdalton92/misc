"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

https://leetcode.com/problems/valid-parentheses/
"""


class BruteForceSolution:
    """Brute force solution.

    Complexity analysis

    Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1)O(1) time.
    Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.
    """

    def is_valid(self, s):
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for char in s:
            # If char is opening bracket
            if char in mapping:
                stack.append(char)
            elif stack:
                elem = stack.pop()
                if char != mapping[elem]:
                    return False
            else:
                return False
        return not stack


if __name__ == "__main__":
    s = "()[]{}"
    obj = BruteForceSolution()
    print(obj.is_valid(s))
