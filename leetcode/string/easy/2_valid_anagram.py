"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

https://leetcode.com/problems/valid-anagram/
"""


class SortingSolution:
    """Sorting Solution.

    O(nlogn) time complexity
    O(1) space complexity
    """

    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False

        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        return s == t

    # def is_anagram(self, s, t):
    #     if len(s) != len(t):
    #         return False
    #     return sorted(s) == sorted(t)


class HashMapSolution:
    """Hash map solution.

    O(nm) time complexity
    O(nm) space complexity
    """

    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False

        hash_map = {}
        for s_char in s:
            if s_char in hash_map:
                hash_map[s_char] += 1
            else:
                hash_map[s_char] = 1
        for t_char in t:
            if t_char in hash_map:
                hash_map[t_char] -= 1
            else:
                return False
        for char in hash_map:
            if hash_map[char] != 0:
                return False
        return True


if __name__ == "__main__":
    s = "rat"
    t = "car"
    instance = HashMapSolution()
    print(instance.is_anagram(s, t))
