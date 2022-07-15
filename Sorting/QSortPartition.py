import random

def partition(x, l, r, pivot):
    ir = l
    r = r - 1
    while ir <= r:
        if x[ir] < pivot:
            x[l], x[ir] = x[ir], x[l]
            l += 1
            ir += 1
        elif x[ir] > pivot:
            x[ir], x[r] = x[r], x[ir]
            r -= 1
        else:
            ir += 1
    return l, ir


def qsort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = x[random.randint(l, r - 1)]
        il, ir = partition(x, l, r, pivot)
        qsort(x, l, il)
        qsort(x, ir, r)


if __name__ == '__main__':
    N = int(input())
    x = list(map(int, input().split()))
    qsort(x)
    print(' '.join(map(str, x)))

