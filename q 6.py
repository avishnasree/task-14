# Program to print the duplicate elements of an array
def duplicate(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates


my_array = [1, 2, 3, 4, 2, 5, 6, 5, 4]
duplicate_elements = duplicate(my_array)
print("Duplicate elements:", duplicate_elements)
