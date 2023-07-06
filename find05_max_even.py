def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    evens=[]
    i=0
    while i<len(data):
        if data[i]%2==0:
            evens.append(data[i])
        i+=1
    max=evens[0]
    i=0
    while i<len(evens):
        
        if max<evens[i]:
            max=evens[i]
       
        i+=1
    return max
numbers=[1,2,6,8,3,4,9,5]
print(find_max_even(numbers))
