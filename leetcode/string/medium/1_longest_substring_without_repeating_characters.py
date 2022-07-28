"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class BruteForceSolution:
    """Solution.

    O(n^2) time complexity
    O(n) space complexity
    """

    def length_of_longest_substring(self, s):
        if not s:
            return 0

        len_s = len(s)
        longest = 1
        for i in range(len_s):
            substring = [s[i]]
            j = i + 1
            while j < len_s:
                if s[j] not in substring:
                    substring.append(s[j])
                    j += 1
                else:
                    break
            longest = max(longest, len(substring))
        return longest


class SlidingWindowSolutions:
    """Solution.

    O(n) time complexity
    O(min(n, m)) space complexity
    """

    def length_of_longest_substring(self, s):
        i = 0
        len_s = len(s)
        longest = 0
        hash_map = {}
        for j in range(len_s):
            if s[j] in hash_map:
                i = max(hash_map[s[j]], i)
            longest = max(longest, j - i + 1)
            hash_map[s[j]] = j + 1

        return longest


if __name__ == "__main__":
    s = "abcabcbb"
    instance = SlidingWindowSolutions()
    print(instance.length_of_longest_substring(s))
