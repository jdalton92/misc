"""
Given an m x n matrix, return all elements of the matrix in spiral order.

https://leetcode.com/problems/spiral-matrix/submissions/
"""


class BoundariesSolution:
    """Boundaries Solution.

    O(mn) time complexity
    O(1) space complexity
    """

    def spiral_order(self, matrix):
        spiral = []
        height = len(matrix)
        width = len(matrix[0])
        up = 0
        down = height - 1
        left = 0
        right = width - 1

        while len(spiral) < height * width:
            # Left to right
            for col in range(left, right + 1):
                spiral.append(matrix[up][col])

            # Top to bottom
            for row in range(up + 1, down + 1):
                spiral.append(matrix[row][right])

            # Ensure we are on a different row
            if up != down:
                # Right to left
                for col in range(right - 1, left - 1, -1):
                    spiral.append(matrix[down][col])

            # Ensure we are on a different column
            if left != right:
                # Bottom to top
                for row in range(down - 1, up, -1):
                    spiral.append(matrix[row][left])

            up += 1
            down -= 1
            left += 1
            right -= 1

        return spiral


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    instance = BoundariesSolution()
    # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    print(instance.method(matrix))
