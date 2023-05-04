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
        if i ==  search_value:
            return i
        elif i > search_value:
            return f"{search_value} does not exist"
    return f'{search_value} does not exist'


# ordered_linear search test
print(ordered_linear_search(test_arr, 54))

# Binary search
def binary_search(array, search_value):
    lower_bound = 0
    upper_bound = len(array)
    
    while lower_bound <= upper_bound:
        midpoint = lower_bound + (upper_bound - lower_bound) // 2
        midpoint_value = array[midpoint]
        
        if search_value == midpoint_value:
            return midpoint_value
        elif search_value > midpoint_value:
            lower_bound = midpoint + 1
        elif search_value < midpoint_value:
            upper_bound = midpoint - 1
    return 
# binary search test
print(binary_search(test_arr, 54))

# selection sort
def selection_sort(array):
    for i in range(len(array)):
        lowest_val_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_val_index]:
                lowest_val_index = j
        
        if lowest_val_index != i:
            array[i], array[lowest_val_index] = array[lowest_val_index], array[i]
    return array
# selection sort test
test_arr = [23, 54, 13, 56, 75 , 75 ,78, 34, 64]
print(selection_sort(test_arr))

# finding duplicates the quadratic way
def hasDuplicates(ls):
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j and ls[i] == ls[j]:
                return f'There is a duplicate {ls[j]}'
print(hasDuplicates(test_arr))     

# finding duplicates the linear way
def linearDuplicateFinder(array):
    largest_element_in_sorted_array = array[-1]
    temp_mem = [" " for i in range( largest_element_in_sorted_array)]
    
    for i in range(len(array)):
        if temp_mem[array[i]] == 1:
            return "Duplicate found"
        else:
            temp_mem[array[i]] = 1
    print(temp_mem)

print(linearDuplicateFinder(test_arr))


# Intersection of two arrays
# def intersection(array1, array2):
#     intersects = []
    
#     for i in range(len(array1)):
#         for j in range(len(array2)):
#             if array1[i] == array2[j]:
#                 intersects.append(array2[j])
#     print(intersects)

def intersection(array1, array2):
    # turn array1 into a hash table
    arrDict = {}
    intersects = []
    for i in array1:
        arrDict[i] = True
    print(arrDict)
    
    for j in array2:
        if j in arrDict.keys():
            intersects.append(j)
                       
    print(intersects)


# testing intersection algorithm
intersection([1, 2, 3, 5, 6, 7], [2, 4, 6, 3, 7])

def first_duplicate(array):
    arrDict = {}
    firstDuplicate = ''
    
    for i in array:
        if i not in arrDict.keys():
            arrDict[i] = True
        else:
            firstDuplicate = i
    print(firstDuplicate)

first_duplicate(["a", "b", "c", "d", "c", "e",
"f"])