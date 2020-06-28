sampleString = "Py"

def stringConcatentor(sampleString):
    if len(sampleString) < 2:
        return ''
    else:
        return sampleString[:2] + sampleString[-2:]


result = print(stringConcatentor(sampleString))