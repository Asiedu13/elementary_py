def hasDuplicates(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if j != i and array[i] == array[j]:
                return 'There are duplicates'
    return 'No duplicates found'


test_arr = [1, 2, 3, 4, 5, 5]
print(hasDuplicates(test_arr))