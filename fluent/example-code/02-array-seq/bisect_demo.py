# BEGIN BISECT_DEMO
import bisect
import sys
import random

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1>
        offset = position * '  |'  # <2>
        print(ROW_FMT.format(needle, position, offset))  # <3>


def demo2():
    random.seed(1)
    print('New pos contents')
    print('-----------------')
    l = []

    for i in range(1, 15):
        r = random.randint(1, 100)
        position = bisect.bisect(l, r)
        bisect.insort(l, r)
        print('%3d %3d' % (r, position), l)


# 可以看到，在插入这些随机数的时候数组同时进行了排序。不过其中有一些重复的元素，比如上面的77,77。
# 你可以对这些重复元素的顺序进行设置，如果希望重复的元素出现在与他相同的元素左边就是用bisect_left，
# 否则就是用bisect_right，相应的使用insort_left和insort_right。比如下面的代码，我们可以看到出现重复的元素索引变化：
# bisect其实是bisect_right的别名
def demo3():
    random.seed(1)
    print('New pos contents')
    print('-----------------')
    l = []

    for i in range(1, 15):
        r = random.randint(1, 100)
        position = bisect.bisect_left(l, r)
        bisect.insort_left(l, r)
        print('%3d %3d' % (r, position), l)


if __name__ == '__main__':

    if sys.argv[-1] == 'left':  # <4>
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5>
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    print("--------demo2-----------")
    demo2()
    print("--------demo3-----------")
    demo3()

# END BISECT_DEMO
