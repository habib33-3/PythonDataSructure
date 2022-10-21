n = 15


def nth_ugly(n):
    ugly = [0] * n
    ugly[0] = 1

    u2 = u3 = u5 = 0

    multiple_2 = 2
    multiple_3 = 3
    multiple_5 = 5

    for i in range(1, n):
        ugly[i] = min(multiple_2, multiple_3, multiple_5)

        if ugly[i] == multiple_2:
            u2 += 1
            multiple_2 = ugly[u2] * 2

        if ugly[i] == multiple_3:
            u3 += 1
            multiple_3 = ugly[u3] * 3

        if ugly[i] == multiple_5:
            u5 += 1
            multiple_5 = ugly[u5] * 5

    return ugly[n - 1]


print(nth_ugly(n))
