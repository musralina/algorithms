import bisect


def myLis(x, l):
    dp = [float("inf")]
    for i in range(l):
        index = bisect.bisect_left(dp, x[i])
        if index >= len(dp):
            dp.append(x[i])
        else:
            dp[index] = x[i]
    return len(dp)


if __name__ == '__main__':
    l = int(input())
    x = list(map(int, input().split()))
    l = myLis(x, l)
    print(l)

