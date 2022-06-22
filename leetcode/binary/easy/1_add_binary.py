"""
Given two binary strings a and b, return their sum as a binary string.

https://leetcode.com/problems/add-binary/
"""


class Solution:
    """Solution.

    Start from carry = 0. If number a has 1-bit in this lowest bit, add 1 to the carry. The
    same for number b: if number b has 1-bit in the lowest bit, add 1 to the carry. At this
    point the carry for the lowest bit could be equal to (00)_2, (01)_2, or (10)_2.

    Now append the lowest bit of the carry to the answer, and move the highest bit of the
    carry to the next order bit.

    Repeat the same steps again, and again, till all bits in a and b are used up. If there
    is still nonzero carry to add, add it. Now reverse the answer string and the job is done

    O(max(n, m)) time complexity
    O(man(n, m)) space complexity
    """

    def add_binary(self, a, b):
        n = max(len(a), len(b))
        # Add zeros to beginning of str so they are the same length
        a = a.zfill(n)
        b = b.zfill(n)

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")
            carry = carry // 2

        if carry == 1:
            answer.append("1")
        answer.reverse()

        return "".join(answer)


if __name__ == "__main__":
    a = "11"
    b = "1"
    instance = Solution()
    print(instance.add_binary(a, b))
