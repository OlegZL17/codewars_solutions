"""
DESCRIPTION:
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    cnt_zeros = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    lst += [0] * cnt_zeros
    return lst