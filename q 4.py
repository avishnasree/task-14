# Find Second Largest Number in Array 
def second_largest(arr):
    arr.sort()
    return arr[-2]

array = [12, 40, 2, 1, 31, 10, 8, 6]
second_largest = second_largest(array)
print("Second largest number is:", second_largest)

