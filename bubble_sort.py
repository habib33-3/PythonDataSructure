def bubble_sort(a):
    iterations = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            iterations += 1
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a, iterations


a = [7, 6, 5, 67, 6, 5, 4, 4, 3, 5]
print(bubble_sort(a))
