import unittest
import src.maxheap as maxheap

def two_vals():
    a = []
    maxheap.maxheappush(a, 6)
    maxheap.maxheappush(a, 5)
    return a

def three_vals():
    a = []
    maxheap.maxheappush(a, 6)
    maxheap.maxheappush(a, 9)
    maxheap.maxheappush(a, 3)
    return a

def four_vals():
    a = []
    maxheap.maxheappush(a, 6)
    maxheap.maxheappush(a, 7)
    maxheap.maxheappush(a, 6)
    maxheap.maxheappush(a, 1)
    return a

class Testmaxheap(unittest.TestCase):
    def test_two_vals(self):
        a = two_vals()
        self.assertEqual(maxheap.getmaxheaproot(a), 6)
        self.assertEqual(len(a), 2)
        self.assertEqual(maxheap.maxheappop(a), 6)
        self.assertEqual(len(a), 1)
        self.assertEqual(maxheap.maxheappop(a), 5)
        self.assertEqual(len(a), 0)
    
    def test_three_vals(self):
        a = three_vals()
        self.assertEqual(maxheap.getmaxheaproot(a), 9)
        self.assertEqual(len(a), 3)
        self.assertEqual(maxheap.maxheappop(a), 9)
        self.assertEqual(len(a), 2)
        self.assertEqual(maxheap.maxheappop(a), 6)
        self.assertEqual(len(a), 1)
        self.assertEqual(maxheap.maxheappop(a), 3)
        self.assertEqual(len(a), 0)

    def test_four_vals(self):
        a = four_vals()
        self.assertEqual(maxheap.getmaxheaproot(a), 7)
        self.assertEqual(len(a), 4)
        self.assertEqual(maxheap.maxheappop(a), 7)
        self.assertEqual(len(a), 3)
        self.assertEqual(maxheap.maxheappop(a), 6)
        self.assertEqual(len(a), 2)
        self.assertEqual(maxheap.maxheappop(a), 6)
        self.assertEqual(len(a), 1)
        self.assertEqual(maxheap.maxheappop(a), 1)
        self.assertEqual(len(a), 0)