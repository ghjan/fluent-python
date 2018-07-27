"""
Container ``in`` operator performance test
"""
import sys
import timeit

SETUP = '''
import array
selected = array.array('d')
with open('selected.arr', 'rb') as fp:
    selected.fromfile(fp, {size})
if {container_type} is dict:
    haystack = dict.fromkeys(selected, 1)
else:
    haystack = {container_type}(selected)
if {verbose}:
    print(type(haystack), end='  ')
    print('haystack: %10d' % len(haystack), end='  ')
needles = array.array('d')
with open('not_selected.arr', 'rb') as fp:
    needles.fromfile(fp, 500)
needles.extend(selected[::{size}//500])
if {container_type} is set:
    needles = set(needles.tolist())
if {verbose}:
    print(type(needles), end='  ')
    print(' needles: %10d' % len(needles), end='  ')
'''

TEST = '''
found = 0
if {container_type} is dict or {container_type} is list:
    for n in needles:
        if n in haystack:
            found += 1
else:
    found = len(needles & haystack)

if {verbose}:
    print('  found: %10d' % found)
'''


def test(container_type, verbose):
    MAX_EXPONENT = 7
    for n in range(3, MAX_EXPONENT + 1):
        size = 10 ** n
        setup = SETUP.format(container_type=container_type,
                             size=size, verbose=verbose)
        test_part = TEST.format(container_type=container_type, verbose=verbose)
        tt = timeit.repeat(stmt=test_part, setup=setup, repeat=5, number=1)
        print('|{:{}d}|{:f}'.format(size, MAX_EXPONENT + 1, min(tt)))


if __name__ == '__main__':
    if '-v' in sys.argv:
        sys.argv.remove('-v')
        verbose = True
    else:
        verbose = False
    if len(sys.argv) != 2:
        print('Usage: %s <container_type>' % sys.argv[0])
    else:
        test(sys.argv[1], verbose)
'''
dict
|    1000|0.000137
|   10000|0.000149
|  100000|0.000284
| 1000000|0.000376
|10000000|0.000434

set
|    1000|0.000110
|   10000|0.000133
|  100000|0.000244
| 1000000|0.000348
|10000000|0.000386

list
|    1000|0.010700
|   10000|0.103838
|  100000|1.047780
| 1000000|10.561153
|10000000|105.547498


'''
