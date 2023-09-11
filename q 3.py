# 3. Write a  program to find the position of a target value within a sorted array using binary search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 9
position = binary_search(sorted_array, target_value)

if position != -1:
    print(f"The target value {target_value} is at position {position}.")
else:
    print("The target value was not found")
