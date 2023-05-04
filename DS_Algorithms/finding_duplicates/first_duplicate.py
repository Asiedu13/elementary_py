def first_duplicate(array):
    arrDict = {}
    duplicates = ''
    for i in array:
        if i in arrDict.keys():
            duplicates = i
            return duplicates
        else:
            arrDict[i] = True

    return 'No Duplicate found'

print(first_duplicate(["a", "b", "c", "d", "c", "e",
"f"]))