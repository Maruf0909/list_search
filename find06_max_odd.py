def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    odd=[]
    i=0
    while i<len(data):
        if data[i]%2==1:
            odd.append(data[i])
        i+=1
    max=odd[0]
    i=0
    while i<len(odd):
        if max<odd[i]:
            max=odd[i]
        i+=1
    return max
numbers=[5,6,4,2,8,4,3]
print(find_max_odd(numbers))
