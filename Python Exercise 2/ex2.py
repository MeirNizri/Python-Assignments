def lastcall(func):
    '''
    This is a decorator that checks whether the current input for the function it decorates is the same as the previous input.
    If so writes an appropriate message with the last output, otherwise it runs the function normally.
    '''
    global prev_input1
    global prev_input2
    global prev_answer
    prev_input1 = None
    prev_input2 = None
    prev_answer = None

    def wrapper(*args, **kwargs):
        global prev_input1
        global prev_input2
        global prev_answer

        # if the parameters are not equal to the previous input run the function, else print the last output
        if args != prev_input1 or kwargs != prev_input2:
            prev_input1 = args
            prev_input2 = kwargs
            prev_answer = func(*args, **kwargs)
            return (prev_answer)
        else:
            print(f'I already told you that the answer is {prev_answer}!')

    return wrapper




from collections.abc import Iterable

class List(list):
    """
    This class is identical to Python's "list" but allows access to elements through a multidimensional array.
    For example:
    mylist = List([
                    [ [1,2,3,33], [4,5,6,66] ],
                    [ [7,8,9,99], [10,11,12,122] ],
                    [ [13,14,15,155], [16,17,18,188] ]
                 ])
    print(mylist[0,1,3]) will return "66"
    """

    def __getitem__(self, indexes):
        if isinstance(indexes, Iterable):
            result = self
            for i in indexes:
                result = result[i]
            return result
        # if the input is not iterable handle it as a regular list
        else:
            return super().__getitem__(indexes)

    def __setitem__(self, indexes, value: object):
        if isinstance(indexes, Iterable):
            result = self
            for i in indexes[:-1]:
                result = result[i]
            result[indexes[-1]] = value
        # if the input is not iterable handle it as a regular list
        else:
            return super().__setitem__(indexes, value)