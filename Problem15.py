def insertStringMiddle(stringInWhichDataIsInserted, stringToBeInserted):
    returnableString = stringInWhichDataIsInserted[:2] + stringToBeInserted + stringInWhichDataIsInserted[-2:]
    return returnableString

print(insertStringMiddle('{{}}','Python'))