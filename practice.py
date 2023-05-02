test_arr = [23, 54, 13, 56, 75 , 78, 34, 64]

# Linear search
def linear_search(array, search_value):
    for i in array:
        if i == search_value:
            return i
    return f'{search_value} does not exist'
# Linear search test
print(linear_search(test_arr, 90))

# Bubble sort
def bubble_sort(array):
    unsorted_until_index = len(array) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        unsorted_until_index -= 1
    return array

# bubble sort test            
print(bubble_sort(test_arr))


# ordered linear search
def ordered_linear_search(array, search_value):
    for i in array:
        if i == search_value:
            return i
        
        elif i > search_value:
            return f'{search_value} does not exist'
    return f'{search_value} does not exist'

# ordered_linear search test
print(ordered_linear_search(test_arr, 50))
        
# Binary search

# binary search test


# selection sort
def selection_sort(array):
    for i in range(len(array)):
        lowest_number_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j
        
        if lowest_number_index != i:
            array[i], array[lowest_number_index] = array[lowest_number_index], array[i]
    return array 

test_arr = [23, 54, 13, 56, 75 , 78, 34, 64]

print(selection_sort(test_arr))