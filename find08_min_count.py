def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    min_count=data[0]
    i=1
    while i<len(data):
        if min_count>data[i]:
            min_count=data[i]
        i+=1

    return data.count(min_count)
numbers=[6,5,3,3,3,8,6,5,9,3,8,5]
print(find_min_count(numbers))
