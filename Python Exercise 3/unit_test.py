import unittest
from bounded_subsets import bounded_subsets

lst1, lst2, lst3, lst4, lst5, lst6 = [], [], [], [], [], []
for s in bounded_subsets([1, 2, 3], 4):
    lst1.append(s)
for s in bounded_subsets([1, 2, 3], 0):
    lst2.append(s)
for s in bounded_subsets([1, 2, 3], 6):
    lst3.append(s)
for s in bounded_subsets([1, 2], 1):
    lst4.append(s)
for s in bounded_subsets([10, 20, 30], 9):
    lst5.append(s)
for s in bounded_subsets([10], 10):
    lst6.append(s)

class MyTestCase(unittest.TestCase):
    def test_bounded_subsets(self):
        self.assertEqual(lst1.sort(), [[], [1], [2], [3], [1, 2], [1, 3]].sort())
        self.assertFalse(lst2)
        self.assertEqual(lst3.sort(), [[], [1], [2], [3], [1, 2], [1, 3], [1, 2, 3]].sort())
        self.assertEqual(lst4.sort(), [[], [1]].sort())
        self.assertFalse(lst5)
        self.assertEqual(lst6.sort(), [[], [10]].sort())
        with self.assertRaises(Exception):
            bounded_subsets([1, -2, 3], 6)
        with self.assertRaises(Exception):
            bounded_subsets([1, 2, 3], -6)

if __name__ == '__main__':
    unittest.main()
