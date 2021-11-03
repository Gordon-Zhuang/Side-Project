def lower_bound(arr, target, i, j):
    while i < j:
        mid = i + (j - i) // 2
        if target < arr[mid]:
            j = mid
        else:
            i = mid + 1
    mid = i + (j - i) // 2
    return mid

print(lower_bound([1,3,5,6,7],4,0,4))