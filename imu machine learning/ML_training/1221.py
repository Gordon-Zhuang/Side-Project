def serch(inter_array, target_value):
    left = 0
    right = len(inter_array) - 1
    while left < right:
        mid = (left + right) // 2
        if inter_array[mid] < target_value:
            left = mid + 1
        else:
            right = mid
    if inter_array[left] == target_value:
        return left
    return -1
print(serch([0,1,2,3,4,5,6,7,8,9], 5))