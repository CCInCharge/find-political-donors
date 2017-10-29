import unittest
from src.MedianHeap import MedianHeap

def init_MedianHeap():
    return MedianHeap()

def one_value(val):
    a = MedianHeap()
    a.add(val)
    return a

def two_values():
    a = MedianHeap()
    a.add(5)
    a.add(3)
    return a

def five_values():
    a = MedianHeap()
    a.add(5)
    a.add(3)
    a.add(7)
    a.add(100)
    a.add(1)
    return a

def round_high():
    a = MedianHeap()
    a.add(5)
    a.add(6)
    a.add(5.75)
    return a

def round_low():
    a = MedianHeap()
    a.add(4)
    a.add(5)
    a.add(4.25)
    return a

class TestMedianHeap(unittest.TestCase):
    def test_init(self):
        heap = init_MedianHeap()
        self.assertEqual(len(heap.left), 0)
        self.assertEqual(len(heap.right), 0)
    
    def test_one_value(self):
        heap = one_value(2)
        self.assertEqual(len(heap.left), 1)
        self.assertEqual(len(heap.right), 0)
        self.assertEqual(heap.median(), 2)

    def test_two_values(self):
        heap = two_values()
        self.assertEqual(len(heap.left), 1)
        self.assertEqual(len(heap.right), 1)
        self.assertEqual(heap.median(), 4)

    def test_five_values(self):
        heap = five_values()
        self.assertEqual(heap.median(), 5)
        self.assertEqual(len(heap.left), 3)
        self.assertEqual(len(heap.right), 2)
    
    def test_round_high(self):
        heap = round_high()
        self.assertEqual(heap.median(), 6)
        self.assertEqual(len(heap.left), 1)
        self.assertEqual(len(heap.right), 2)

    def test_round_low(self):
        heap = round_low()
        self.assertEqual(heap.median(), 4)
        self.assertEqual(len(heap.left), 1)
        self.assertEqual(len(heap.right), 2)

if __name__ == "__main__":
    unittest.main()