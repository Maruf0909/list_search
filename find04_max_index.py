def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    max=data[0]
    i=1
    while i<len(data):
        if max<data[i]:
            max=data[i]
        i+=1
    return data.index(max)
numbers=[1,9,8,4,5]
print(find_max_index(numbers))
