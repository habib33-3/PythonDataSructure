def search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return start


a = [3, 4, 6, 8, 13, 56, 88, 333, 55, 7, 11, 98, 44, 23, 55]
t = 88
result = search(a, 0, len(a) - 1, t)
print(result)
