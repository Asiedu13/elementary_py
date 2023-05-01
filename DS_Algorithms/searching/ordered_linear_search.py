# There is another condition that makes sure we don't check for values greater than the search value since the array is arranged in ascending order.

def ordered_linear_search(array, search_value):
    for i in array:
        if i == search_value:
            return i
        elif i > search_value:  
            return 'Does not exist'
    return 'Does not exist'


test_arr = [i for i in range(300)]

print(ordered_linear_search(test_arr, 50))