def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


a = [2, 3, 5, 8, 0, 10, 18]
Target = 5
print(search(a, Target))
