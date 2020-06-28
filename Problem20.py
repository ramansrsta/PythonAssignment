def stringMatchCounter(list):
    counter=0
    for words in list:
        if len(words) > 2 and words[0] == words[-1]:  
            counter += 1
    return counter

print(stringMatchCounter(['abc', 'xyzx', 'aba', '1221']))