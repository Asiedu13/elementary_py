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
def binary_search(array, search_value):
    lower_boundary = 0
    upper_boundary = len(array)
    
    while lower_boundary <= upper_boundary:
        midpoint = lower_boundary + (upper_boundary - lower_boundary) // 2
        midpoint_value = array[midpoint]
        
        if search_value == midpoint_value:
            return midpoint_value
        elif search_value > midpoint_value:
            lower_boundary = midpoint + 1
        elif search_value < midpoint_value:
            upper_boundary = midpoint - 1
    return f'{search_value} does not exist' 
# binary search test
print(binary_search(test_arr, 23))