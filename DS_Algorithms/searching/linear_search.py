def linear_search(array, search_value):
    for i in array:
        if search_value == i:
            return i
        else:
            continue
    return "Does not exist in this list"

test_arr = [i for i in range(30)]

print(linear_search(test_arr, 35))


def linear_search_(array, search_value):
    for i in range(len(array)):
        if search_value == array[i]:
            return i
    return 'Does not exist'

print(linear_search_(test_arr, 35))