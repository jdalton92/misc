"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

https://leetcode.com/problems/backspace-string-compare/
"""


class Solution:
    """Solution.

    O(n + m) time complexity
    O(n + m) space complexity
    """

    def parse_string(self, str):
        len_str = len(str)
        parsed_str = []
        for i in range(len_str):
            if str[i] == "#":
                if parsed_str:
                    parsed_str.pop()
            else:
                parsed_str.append(str[i])

        return parsed_str

    def backspace_compare(self, s, t):
        return self.parse_string(s) == self.parse_string(t)


if __name__ == "__main__":
    s = "y#fo##f"
    t = "y#f#o##f"
    instance = Solution()
    print(instance.backspace_compare(s, t))
    # True
