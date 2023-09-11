# Program to copy all elements of one array into another array

def array(arr1):
    arr2 = []
    for element in arr1:
        arr2.append(element)
    return arr2


array1 = [1, 2, 3, 4, 5]
array2 = array(array1)
print("output:", array2)
