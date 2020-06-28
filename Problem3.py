sampleString = 'restartingr'

def firstStringReplacer(str1):
    firstString = str1[0]
    replacedString = str1.replace(firstString, '$')
    finalString = firstString + replacedString[1:]
    return finalString

result = print(firstStringReplacer(sampleString))