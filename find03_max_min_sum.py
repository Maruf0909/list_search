def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    max=data[0]
    min=data[0]
    i=1
    while i<len(data):
        if max<data[i]:
            max=data[i]
        
        if min>data[i]:
            min=data[i]
        i+=1
        sum=max+min
    return sum
numbers=[5,7,3,4,8]
print(find_max_min_sum(numbers))
