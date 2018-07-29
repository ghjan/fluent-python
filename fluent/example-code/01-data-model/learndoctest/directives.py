# _*_ coding: utf-8 _*_
'''
>>> print(list(range(20))) # doctest: +NORMALIZE_WHITESPACE
[0,   1,  2,  3,  4,  5,  6,  7,  8,  9,
10,  11, 12, 13, 14, 15, 16, 17, 18, 19]

>>> print(list(range(20))) # doctest: +ELLIPSIS
[0, 1, ..., 18, 19]

>>> print(list(range(5)) + list(range(10, 20)) + list(range(30, 40)))
... # doctest: +ELLIPSIS
[0, ..., 4, 10, ..., 19, 30, ..., 39]

# >>> 1./7  # risky
# 0.14285714285714285
# >>> print(1./7) # safer
# 0.142857142857
>>> print(round(1./7, 6)) # much safer
0.142857
'''

if __name__ == "__main__":
    import doctest

    doctest.testmod()
