"""
Here is a set of wrapper functions built on Python's built-in heapq library.
heapq only contains an implementation of min-heaps. This module has several
methods to mimic the functionality of a max-heap.
"""

import heapq
def maxheappush(heap, item):
    """
    Push the value item onto the max heap, maintaining the heap invariant.

    :param heap: List which has the heap property
    :param item: Value to add to the heap
    """
    heapq.heappush(heap, -item)

def maxheappop(heap):
    """
    Pop and return the largest item from the max heap, maintaining the heap
    invariant. If the heap is empty, IndexError is raised.
    Do not access the root value with heap[0] - use the getmaxheaproot function
    instead.

    :param heap: List which has the heap property
    :returns:    The maximum value in this heap
    """
    root = heapq.heappop(heap)
    return -root

def getmaxheaproot(heap):
    """
    Returns the largest item from the max heap, without popping it.

    :returns: The maximum value in this heap
    """
    return heap[0] * -1