from math import factorial


def permute(string):
    for p in range(factorial(len(string))):
        print(''.join(string))
        i = len(string) - 1
        while i > 0 and string[i - 1] > string[i]:
            i -= 1
        string[i:] = reversed(string[i:])
        if i > 0:
            q = i
            while string[i - 1] > string[q]:
                q += 1
            temp = string[i - 1]
            string[i - 1] = string[q]
            string[q] = temp


s = 'abc'
s = list(s)

permute(s)
