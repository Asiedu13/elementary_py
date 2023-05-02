def selection_sort(array):
    for i in range(len(array)):
        lowest_number_index = i
        for j in range( i + 1, len(array)):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j
        if lowest_number_index != i:
            array[i], array[lowest_number_index] = array[lowest_number_index], array[i]
        
        print(array)
        
    return array

test_arr = [12, 45, 65, 23, 75, 0]
print(selection_sort(test_arr))