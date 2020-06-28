def smallestOfList(list):
    small = list[0]
    for index in range(len(list)):
        if  list[index] < small:
            small = list[index]
        else:
            pass 
    return small

print(smallestOfList([14,14,5,7]))

