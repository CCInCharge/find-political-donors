"""
MedianHeap is a class designed to store streaming data and be able to
efficiently calculate the median, sum, and size of the data set. It utilizes
a pair of heaps (a min heap and a max heap) to calculate the running median
in O(1) time (at the cost of maintaining the two heaps, which takes O(log n)
time). This is much more efficient than calculating a median from a large
data set by sorting it.
"""

import heapq
import src.maxheap as maxheap

class MedianHeap:
    def __init__(self):
        """
        Initializes MedianHeap class with two attributes: left and
        right heaps. left is a max heap of the smaller half of the data, and
        right is a min heap of the larger half of the data.
        """
        # left is a max heap of the lower half of the data
        # right is a min heap of the upper half of the data
        self.left = []
        self.right = []
        self.sum = 0

    def __rebalance(self):
        """
        Algorithm only works if the heaps are balanced, i.e., if the left and
        right arrays have a size difference of at most one. This method
        rebalances the arrays so that this property is maintained.
        """
        left_len = len(self.left)
        right_len = len(self.right)
        if left_len == right_len or abs(right_len - left_len) == 1:
            return
        elif left_len > right_len:
            heapq.heappush(self.right, maxheap.maxheappop(self.left))
        else:
            maxheap.maxheappush(self.left, heapq.heappop(self.right))
        
    def add(self, val):
        """
        Adds a new value to the data.
        
        :param val: Value to add
        """
        # Accounts for edge case, when there is no data yet
        if not self.left or val <= maxheap.getmaxheaproot(self.left):
            maxheap.maxheappush(self.left, val)
        else:
            heapq.heappush(self.right, val)
        self.sum += val
        self.__rebalance()
    
    def median(self):
        """
        Calculates the median of the data.

        :returns: Median of data. If there is no data, returns None
        """
        left_len = len(self.left)
        right_len = len(self.right)
        if not self.left and not self.right:
            return None
        elif left_len > right_len:
            return int(round(maxheap.getmaxheaproot(self.left), 0))
        elif right_len > left_len:
            return int(round(self.right[0], 0))
        elif left_len == right_len:
            median = (maxheap.getmaxheaproot(self.left) + self.right[0]) / 2.0
            return int(round(median, 0))
    
    def length(self):
        """
        Returns the number of data points available.

        :returns: int, number of data points. Returns 0 if no data.
        """
        return len(self.left) + len(self.right)