sampleString = "Insight Workshop"
characterCounterDictionary = {}

for character in sampleString:
    if character in characterCounterDictionary:
        characterCounterDictionary[character] += 1
    else:
        characterCounterDictionary[character] = 1
        
print('The frequency of character is ', characterCounterDictionary)