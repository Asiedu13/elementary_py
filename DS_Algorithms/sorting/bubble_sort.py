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

test_array = [23, 24, 12, 64, 35, 78, 23, 45, 25, 73, 54]

print(bubble_sort(test_array))
