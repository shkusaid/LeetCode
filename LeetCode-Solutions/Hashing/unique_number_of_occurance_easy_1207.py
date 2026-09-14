def unique_number_of_occurance(array):
    freq = {}
    for arr in array:
        freq[arr] = freq.get(arr , 0) + 1
    present = set()
    for val in freq.values():
        if val in present:
            return False
        present.add(val)
    return True

array = [1,2,2,1,1,3]
print(unique_number_of_occurance(array))

array = [1,2]
print(unique_number_of_occurance(array))