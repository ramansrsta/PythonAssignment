
def longestWord(listOfWords):
    max =len(listOfWords[0])
    for word in listOfWords:
        if max < len(word):
            max = len(word)
    print(max)

longestWord(["Languages", "Writings", "Prodigyingly", "Asparaguses"])
