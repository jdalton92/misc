"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

https://leetcode.com/problems/flood-fill/
"""


class DepthFirstSearchSolution:
    """Depth First Search Solution.

    O(n) time complexity where n is the number of pixels
    O(n) space complexity where n is the number of pixels
    """

    def flood_fill(self, image, sr, sc, color):
        height = len(image)
        width = len(image[0])
        starting_color = image[sr][sc]

        def fill(sr, sc):
            if image[sr][sc] == starting_color:
                image[sr][sc] = color
                if sr - 1 >= 0:
                    fill(sr - 1, sc)
                if sr + 1 < height:
                    fill(sr + 1, sc)
                if sc - 1 >= 0:
                    fill(sr, sc - 1)
                if sc + 1 < width:
                    fill(sr, sc + 1)

        fill(sr, sc)
        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    instance = DepthFirstSearchSolution()
    print(instance.flood_fill(image, sr, sc, color))
