import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import ArrayLike
from scipy.optimize import fsolve

def plotIntersection(x_range: ArrayLike, f1: callable, f2: callable) -> None:
    """
    plot two functions and their intersection in range of x values

    Parameters
    ----------
    x_range : array-like
        The horizontal coordinates of the data points.
    f1, f2 : callable f(x)
        A function that takes one (possibly vector) argument,
        and returns a value of the same length.

    example:
    >>> f = lambda x: x ** 2
    >>> g = lambda x: x + 10
    >>> plotIntersection(np.linspace(-10, 10, 1000), f, g)

    """

    # find all intersection in x_range
    def verify_intersection(x):
        return (abs(f1(x) - f2(x)) < 0.001
                and x_range[0] <= x <= x_range[-1])
    intersect_candidates = fsolve(lambda x: f1(x) - f2(x), np.arange(x_range[0], x_range[-1]))
    intersections = np.array([x for x in intersect_candidates if verify_intersection(x)])

    # plot the functions in x_range and their intersections
    plt.plot(x_range, f1(x_range))
    plt.plot(x_range, f2(x_range))
    plt.plot(intersections, f1(intersections), 'ro')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
