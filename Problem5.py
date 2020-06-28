
def ingAdder(sampleString):
    if len(sampleString) < 3:
        return sampleString
    else:
        if sampleString[-3:] == 'ing':
            sampleString += 'ly'
            return sampleString
        else:
            sampleString +='ing'
            return sampleString
    

result = print(ingAdder('abc'))