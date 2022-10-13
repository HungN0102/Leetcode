# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
import math

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

def fullJustify(words, maxWidth):
    output = []

    i = 0
    while i <= len(words) - 1:
        widthRemain = maxWidth + 1
        currentWords = []
        while i <= len(words) - 1 and widthRemain - len(words[i]) - 1 >= 0:
            currentWords.append(words[i])
            widthRemain -= (len(words[i]) + 1)
            i += 1

        widthRemain += len(currentWords) - 1
        spaceEachWord = math.ceil(widthRemain / max(1,(len(currentWords) - 1)))

        currentString = ""
        for w in currentWords:
            currentString += w 
            currentString += " " * int(min(widthRemain, spaceEachWord))
            widthRemain -= min(widthRemain, spaceEachWord)


        output.append(currentString)
    return output 

fullJustify(words, maxWidth)
