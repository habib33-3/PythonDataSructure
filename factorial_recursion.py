def factorial(n):
    if n == 1:
        return n
    else:
        temp = factorial(n - 1)
        temp *= n
    return temp


print(factorial(6))
