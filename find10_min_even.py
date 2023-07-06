def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    evens=[]
    i=0
    while i<len(data):
        if data[i]%2==0:
            evens.append(data[i])
        i+=1
    
    min=evens[0]
    i=0
    while i<len(evens):
        if min>evens[i]:
            min=evens[i]
        i+=1    


    return min
numbers=[4,7,6,9,21,6,8]
print(find_min_even(numbers))

