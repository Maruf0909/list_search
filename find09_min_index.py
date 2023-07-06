def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    min_index=data[0]
    i=1
    while i<len(data):
        if min_index>data[i]:
            min_index=data[i]
        i+=1
    return data.index(min_index)
numbers=[8,7,3,6,1,2,3,4,5,6,7]
print(find_min_index(numbers))

