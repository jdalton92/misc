"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

https://leetcode.com/problems/valid-palindrome/
"""


class IterativeSolution:
    """Iterative Solution.

    O(n) time complexity
    O(n) space complexity
    """

    def is_palindrome(self, s):
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = list(map(lambda ch: ch.lower(), filtered_chars))
        length = len(lowercase_filtered_chars)
        for i in range(length):
            if lowercase_filtered_chars[i] != lowercase_filtered_chars[length - 1 - i]:
                return False
        return True


class CompareWithReverseSolution:
    """Compare With Reverse Solution.

    O(n) time complexity
    O(n) space complexity
    """

    def is_palindrome(self, s):
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = list(map(lambda ch: ch.lower(), filtered_chars))
        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    instance = CompareWithReverseSolution()
    print(instance.is_palindrome(s))
