def safe_call(func: callable, **kwargs):
    '''
    Gets as input a function and parameters with names, and calls the function with the arguments,
    but only if they correspond exactly to the types defined in the annotation of the function.
    If the types do not match, an exception will be thrown describing what type of argument was received
    and what type the function expected.
    '''
    import inspect
    annotations = inspect.getfullargspec(func).annotations
    for x in annotations:
        if type(kwargs[x]) is not annotations[x]:
            raise Exception(f'{x} is invalid argument, expected {annotations[x]} and gets {type(kwargs[x])}')
    return func(**kwargs)


import copy
from collections.abc import Iterable

def print_sorted(collec):
    '''
    Gets as input some deep collection consisting of lists, tupples, sets, and dictionaries.
    And prints it when it is sorted at all levels, i.e. all values at all levels are sorted
    in ascending order. The entries in the dictionary are arranged in ascending order of the keys.
    '''
    def sort(var):
        '''
        Auxillary function. Gets as input some deep collection consisting of lists, tupples,
        sets, and dictionaries. Return the collection when it is sorted in all levels using recursion.
        '''
        if isinstance(var, dict):
            for key in var:
                var[key] = sort(var[key])
            var = sorted(var.items(), key=lambda x: str(x))
        elif isinstance(var, Iterable):
            for i, x in enumerate(var):
                var = list(var)
                var[i] = sort(x)
            var = sorted(var, key=lambda x: str(x))
        return var

    collec_copy = copy.deepcopy(collec)
    sorted_collec = sort(collec_copy)
    print(sorted_collec)
    return sorted_collec


def find_root(f: callable, a: float, b: float):
    '''
    Gets as input a real function and a range [a,b], and finds
    the function root in the range defined by the numbers.
    '''
    assert (a <= b)
    eps = 0.00001

    def derive_f(y: float):
        return (f(y + eps) - f(y)) / eps

    x1 = a
    x2 = b
    while abs(x2 - x1) >= eps:
        x2 = x1
        x1 = x2 - f(x2) / derive_f(x2)
    return x1
