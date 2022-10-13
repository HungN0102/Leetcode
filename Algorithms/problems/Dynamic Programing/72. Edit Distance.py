def levenshteinDistance(str1, str2):
    str1 = " " + str1
    str2 = " " + str2
    
    results = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    for index1 in range(len(str1)):
        results[index1][0] = index1

    for index2 in range(len(str2)):
        results[0][index2] = index2
        
    for index1 in range(1,len(str1)):
        for index2 in range(1,len(str2)):
            if str1[index1] == str2[index2]:
                results[index1][index2] = results[index1-1][index2-1]
                continue
            results[index1][index2] = 1 + min(results[index1][index2-1],results[index1-1][index2],results[index1-1][index2-1])

    return results[-1][-1]

str2 = "abc"
str1 = "yabd"
levenshteinDistance(str1, str2)