def find_bounded_subsets(lst: list, lim: int):
    if any(elem < 0 for elem in lst) or lim < 0:
        raise TypeError("the list and limit must be all positive")

    # if the list is empty return empty list
    if not lst:
        return []

    # get in recursion all valid subsets that doesn't contain the last element
    last_elem = lst[-1]
    ans_without_last = find_bounded_subsets(lst[:-1], lim)

    ans_with_last = []
    if last_elem <= lim:
        ans_with_last.append([last_elem])

    # For each valid subset check whether adding the last element also yields a valid subset
    for subset in ans_without_last:
        if sum(subset)+last_elem <= lim:
            ans_with_last.append(subset+[last_elem])

    return ans_without_last + ans_with_last + []

class bounded_subsets:
    """
    An iterator that receives as input a list of positive numbers - lst, and some positive number - lim,
    and returns a series of all subsets of lst whose sum is at most lim.
    """
    def __init__(self, lst: list, lim: int):
        self.state = []
        self.all_bounded_subsets = find_bounded_subsets(lst, lim).__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        return self.all_bounded_subsets.__next__()
