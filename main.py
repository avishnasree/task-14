# python program to sort even placed elements in increasing and odd placed in decreasing order

def sort_even_odd(arr):
    even = arr[::2]
    odd = arr[1::2]

    even.sort()
    odd.sort(reverse=True)
    result = []
    i, j = 0, 0
    for k in range(len(arr)):
        if k % 2 == 0:
            result.append(even[i])
            i += 1
        else:
            result.append(odd[j])
            j += 1

    return result

input_list = [6, 4, 3, 1, 5, 2]
sorted_list = sort_even_odd(input_list)
print(sorted_list)

