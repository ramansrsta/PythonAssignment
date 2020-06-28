def oddStringRemover(string):
    newString = ""
    for index in range(len(string)):
        if index % 2 == 0:
            newString = newString + string[index]
    return newString

print(oddStringRemover('rinkafjldksajfkdj'))