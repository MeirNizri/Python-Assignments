import unittest
import numpy as np
from matplotlib import pyplot as plt
from plot_Intersection import plotIntersection

class Tests(unittest.TestCase):
    def test_two_intersections(self):
        plt.title("two intersections")
        f = lambda x: x ** 2
        g = lambda x: x + 10
        plotIntersection(np.linspace(-10, 10, 1000), f, g)

    def test_three_intersections(self):
        plt.title("three intersections")
        f = lambda x: np.sin(x)
        g = lambda x: 0.2 * x
        plotIntersection(np.linspace(-10, 10, 1000), f, g)

    def test_many_intersections(self):
        plt.title("many intersections")
        f = lambda x: np.sin(x)
        g = lambda x: np.cos(x)
        plotIntersection(np.linspace(-10, 10, 1000), f, g)

    def test_no_intersections(self):
        plt.title("no intersections")
        f = lambda x: x ** 2
        g = lambda x: x - 25
        plotIntersection(np.linspace(-10, 10, 1000), f, g)

if __name__ == '__main__':
    unittest.main()
