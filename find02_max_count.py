def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    max=data[0]
    i=1
    while i<len(data):
        if max<data[i]:
            max=data[i]
        i+=1
    return data.count(max)
numbers=[1,8,2,8,3,8,4,8,5]
print(find_max_count(numbers))
    