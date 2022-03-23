from ex2 import lastcall, List
import unittest


@lastcall
def f(x: int):
    return x ** 2
@lastcall
def f1(x: str):
    return x.lower()
@lastcall
def f2(x: List[int]):
    return x[0]


mylist = List([
    [[1, 2, 3, 33], [4, 5, 6, 66]],
    [[7, 8, 9, 99], [10, 11, 12, 122]],
    [[13, 14, 15, 155], [16, 17, 18, 188]]
])
mylist1 = List([['a', 'b', 'c', 'd'], [4, 5, 6, 7]])


class Tests(unittest.TestCase):
    def testLasteCall(self):
        self.assertEqual(f(2), 4)
        self.assertEqual(f(2), None)
        self.assertEqual(f(4), 16)
        self.assertEqual(f(4), None)
        self.assertEqual(f(4), None)
        self.assertEqual(f1('ABC'), 'abc')
        self.assertEqual(f1('ABC'), None)
        self.assertEqual(f1('ABC'), None)
        self.assertEqual(f1('ABCD'), 'abcd')
        self.assertEqual(f2([0, 1, 2]), 0)
        self.assertEqual(f2([0, 1, 2]), None)
        self.assertEqual(f2([0, 1, 2]), None)
        self.assertEqual(f2([0, 1]), 0)

    def testList(self):
        self.assertEqual(mylist[0, 1, 3], 66)
        self.assertEqual(mylist[0], [[1, 2, 3, 33], [4, 5, 6, 66]])
        mylist[0, 1, 3] = 50
        self.assertEqual(mylist[0, 1, 3], 50)
        with self.assertRaises(Exception):
            mylist[0, 1, 3, 0]
        with self.assertRaises(Exception):
            mylist[0, 1, 3, 0] = 0
        with self.assertRaises(Exception):
            mylist[10]
        with self.assertRaises(Exception):
            mylist[10] = 0
        self.assertEqual(mylist1[0, 1], 'b')
        self.assertEqual(mylist1[0], ['a', 'b', 'c', 'd'])
        mylist1[1, 3] = 50
        self.assertEqual(mylist1[1, 3], 50)

if __name__ == '__main__':
    unittest.main()