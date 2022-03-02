from ex1 import safe_call, find_root, print_sorted
import unittest

def f1(x: int, y: float, z):
    return x + y + z
def f2(x, y: str):
    return y
def f3():
    return 'ok'

class Tests(unittest.TestCase):
    def testSafeCall(self):
        self.assertEqual(safe_call(f1, x=5, y=7.0, z=3), 15.0)
        self.assertEqual(safe_call(f1, x=5, y=7.0, z=0), 12.0)
        with self.assertRaises(Exception):
            safe_call(f1, x=5, y="abc", z=3)
        self.assertEqual(safe_call(f2, x=5, y="abc"), 'abc')
        with self.assertRaises(Exception):
            safe_call(f1, x=5, y=[])
        self.assertEqual(safe_call(f3), 'ok')

    def testPrintSorted(self):
        self.assertEqual(print_sorted([]), [])
        self.assertEqual(print_sorted([1]), [1])
        self.assertEqual(print_sorted([3,2.0,1]), [1,2.0,3])
        self.assertEqual(print_sorted([4, 3, 2, [-1, 0, -2, 7]]), [2, 3, 4, [-1, -2, 0, 7]])
        self.assertEqual(print_sorted([4, 3, 2, (-1, 0, -2, [11,10])]), [2, 3, 4, [-1, -2, 0, [10,11]]])
        self.assertEqual(print_sorted({"a": 5, "c": 6, "b": [1, 0, 2, 4]}), [('a', 5), ('b', [0, 1, 2, 4]), ('c', 6)])

    def testFindRoot(self):
        self.assertAlmostEqual(find_root(lambda x: x-10, -10, 10), 10)
        self.assertAlmostEqual(find_root(lambda x: x**2-4, 1, 3), 2)
        self.assertAlmostEqual(find_root(lambda x: x**2-4, -3, 1), -2)
        self.assertAlmostEqual(find_root(lambda x: x**3-27, 1, 5), 3)
        self.assertAlmostEqual(find_root(lambda x: x**3-27, 1, 5), 3)
        self.assertAlmostEqual(find_root(lambda x: x**3-10*x+3, 2, 10), 3)
        self.assertAlmostEqual(find_root(lambda x: x**3-10*x+3, 2, 100), 3)
        self.assertAlmostEqual(find_root(lambda x: 0, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()