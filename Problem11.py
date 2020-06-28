sampleString = "My name is Bob and his name is Romeo"

sampleStringSplittted = sampleString.split()
counterDictionary = {}
for word in sampleStringSplittted:
    if word in counterDictionary:
        counterDictionary[word] += 1
    else:
        counterDictionary[word] =1

print(counterDictionary)
