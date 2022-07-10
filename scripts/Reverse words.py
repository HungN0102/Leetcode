def reverseWordsInString(string):
    outputString = ""
    windowEnd = len(string) - 1
    windowStart = len(string) - 1

    if len(string) == 0:
        return outputString
    elif len(string) == 1:
        return string
        
    while windowStart > 0:
        leftChar = string[windowStart]
        if leftChar == " ":
            outputString += string[windowStart+1:windowEnd+1]
            while string[windowStart] == " " and windowStart >= 0:
                outputString += " "
                print(windowStart)
                windowStart -= 1
                windowEnd = windowStart
        else:
            windowStart -= 1
    if string[windowStart] != " ":
        outputString += string[windowStart:windowEnd+1]
        
    return outputString


reverseWordsInString("the sky is blue")