def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    odd=[]
    i=0
    while i<len(data):
        if data[i]%2==1:
            odd.append(data[i])
        i+=1

    min=odd[0]
    i=0
    while i<len(odd):
        if min>odd[i]:
            min=odd[i]
        i+=1
    return min
numbers=[7,4,8,3,2,9,5]
print(find_min_odd(numbers))

    

