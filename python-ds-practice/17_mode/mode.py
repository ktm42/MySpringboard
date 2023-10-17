def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    from collections import Counter

    lst = Counter(nums)
    most_common = lst.most_common()
    val = most_common[0]
    return val[0]

print(mode([1, 2, 4, 5, 4, 6, 4, 7,4]))
