"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

https://leetcode.com/problems/longest-palindrome/
"""


class HashMapSolution:
    """Hash Map Solution.

    O(n) time complexity
    O(n) space complexity
    """

    def longest_palindrome(self, s):
        hash_map = {}
        palindrome_length = 0
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        for char in hash_map:
            palindrome_length += 2 * (hash_map[char] // 2)
        if len(s) > palindrome_length:
            palindrome_length += 1
        return palindrome_length


class UnpairedSolution:
    """Track unpaired chars.

    O(n) time complexity
    O(n) space complexity
    """

    def longest_palindrome(self, s):
        pairs = 0
        unpaired_chars = set()

        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)

        longest_palindrome = pairs * 2
        if unpaired_chars:
            longest_palindrome += 1

        return longest_palindrome


if __name__ == "__main__":
    s = "abccccdd"
    instance = UnpairedSolution()
    print(instance.longest_palindrome(s))
