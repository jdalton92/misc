"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

https://leetcode.com/problems/k-closest-points-to-origin/
"""


import heapq


class SortSolution:
    """Sort Solution.

    O(nlogn) time complexity (worst case for sorting algorithm)
    O(logn) to O(n) space complexity for the sorting algorithm
    """

    def k_closest(self, points, k):
        points.sort(key=lambda key: key[0] ** 2 + key[1] ** 2)
        return points[:k]


class MaxHeapSolution:
    """Max Heap Solution.

    * Use a max heap (or max priority queue) to store points by distance.
        * Store the first kk elements in the heap.
        * Then only add new elements that are closer than the top point in the heap
        while removing the top point to keep the heap at kk elements.

    * Return an array of the kk points stored in the heap.

    O(nlogk) time complexity
    O(k) space complexity
    """

    def k_closest(self, points, k):
        # Since heap is sorted in increasing order, negate the distance to simulate max
        # heap and fill the heap with the first k elements of points
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest, discard the farthest
                # point and add this one
                heapq.heappushpop(heap, (dist, i))

        return [points[i] for (_, i) in heap]

    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2


if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    k = 1
    instance = MaxHeapSolution()
    print(instance.k_closest(points, k))
