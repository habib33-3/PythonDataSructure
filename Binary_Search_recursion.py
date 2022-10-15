def search(arr, start, end, target):
    if end >= start:
        mid = start + end - 1 // 2

        if arr[mid] < target:
            search(a, mid + 1, end, t)
        elif arr[mid] > target:
            return search(a, start, mid - 1, t)
        else:
            return mid
    else:
        return -1


a = [23, 44, 5656, 333, 34, 428, 441, 5, 26, 33, 99]
t = 26
print(search(a, 0, len(a) - 1, t))
