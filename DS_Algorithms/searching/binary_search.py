import math
def binary_search(array, search_value):
    
    lower_boundary = 0
    upper_boundary = len(array) - 1
    
    while lower_boundary <= upper_boundary:
        # midpoint = math.floor((lower_boundary + upper_boundary) / 2)
        midpoint = lower_boundary + (upper_boundary - lower_boundary) // 2
        midpoint_value = array[midpoint]
        
        if search_value == midpoint_value:
            return midpoint_value
        elif search_value > midpoint_value:
            lower_boundary = midpoint + 1
        elif search_value < midpoint_value:
            upper_boundary = midpoint - 1
    return 'Value does not exist'

test_arr = [i for i in range(30)]

print(binary_search(test_arr, 10))
print(binary_search(test_arr, 20))
print(binary_search(test_arr, 30))