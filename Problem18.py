def maximumOfList(list):
    max = list[0]
    for index in range(len(list)):
        if max < list[index]:
            max = list[index]
        else:
            pass 
    return max

print(maximumOfList([1,14,5,7]))

