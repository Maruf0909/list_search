def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    min=data[0]
    i=1
    while i<len(data):
        if min>data[i]:
            min=data[i]
        i+=1
    return min
numbers=[3,1,5,2,9,6]
print(find_min(numbers))


    