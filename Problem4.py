# sampleString = 'abc,xyz'

# stringList = sampleString.split(',')

# string1 = stringList[0]
# string2 = stringList[1]

# lastCharOfString1 = string1[-1:]
# lastCharOfString2 = string2[-1:]

# newString1 = string1[0:-1] + lastCharOfString2 
# newString2 = string2[0:-1] + lastCharOfString1

# finalString = newString1 + ' ' + newString2

# print(finalString)


def stringExchanger(str1,str2):
    newStr1 = str2[0:2] + str1[2:]
    newStr2 = str1[0:2] + str2[2:]

    return newStr1 + ' ' + newStr2

result = print(stringExchanger('abc','xyz'))
