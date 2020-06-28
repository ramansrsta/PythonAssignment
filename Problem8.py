def characterRemover(str,index):
    firstHalf = str[:index]
    lastHalf = str[index+1:]

    print(firstHalf+lastHalf)

characterRemover('Ninja',1)
characterRemover('Shroud',2)
characterRemover('Dynamo',3)