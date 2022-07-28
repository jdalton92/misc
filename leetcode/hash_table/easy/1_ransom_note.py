"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

https://leetcode.com/problems/ransom-note/
"""


import collections


class OneHashMapSolution:
    """One hash map solution.

    O(nm) time complexity
    O(1) space complexity (as max length of hash_map is 26, so this is a constant)
    """

    def can_construct(self, ransom_note, magazine):
        if len(magazine) < len(ransom_note):
            return False

        hash_map = {}
        for char in magazine:
            if hash_map.get(char):
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        for char in ransom_note:
            if hash_map.get(char):
                hash_map[char] -= 1
            else:
                return False
        return True


class TwoHashMapSolution:
    """Two hash map solution.

    O(m) time complexity
    O(1) space complexity (as max length of hash_map is 26, so this is a constant)
    """

    def can_construct(self, ransom_note, magazine):
        if len(magazine) < len(ransom_note):
            return False

        magazine_hash_map = collections.Counter(magazine)
        ransom_note_hash_map = collections.Counter(ransom_note)

        for char, count in ransom_note_hash_map.items():
            if magazine_hash_map[char] < count:
                return False
        return True


if __name__ == "__main__":
    ransom_note = "aa"
    magazine = "aab"
    instance = OneHashMapSolution()
    print(instance.can_construct(ransom_note, magazine))
