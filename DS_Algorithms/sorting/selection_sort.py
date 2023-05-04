def selection_sort(array):
    for i in range(len(array)):
        lowest_number_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j
        if lowest_number_index != i:
            array[i], array[lowest_number_index] = array[lowest_number_index], array[i]
        
        print(array)
        
    return array

test_arr = [23, 54, 13, 56, 75 , 78, 34, 64]
print(selection_sort(test_arr))