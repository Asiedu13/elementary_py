def hasDuplicates(array):
    dup_mem = [ 0 for i in range(8) ] # The range must be the largest value in the array.
    print(dup_mem)
    for i in range(len(array)):
        if dup_mem[array[i]] == 1:
            return 'There are duplicates'
        else:
           dup_mem[array[i]] = 1
            
    print(dup_mem)
    return 'There are no duplicates'

print(hasDuplicates([1, 2, 3, 3, 5, 6, 7]))
