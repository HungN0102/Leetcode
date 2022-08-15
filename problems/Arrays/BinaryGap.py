# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

def solution(number):
    binary = format(number, "b")
    maxCount = 0
    
    i = 0
    if i <= len(binary) - 1 and binary[i] == '1' and binary[i+1] == '0':
        count = 0
        while i + 1<= len(binary) - 1 and binary[i+1] == '0':
            count += 1
            i += 1
        if i + 1 <= len(binary) - 1 and binary[i+1] == '1':
            maxCount = max(maxCount, count)
            i += 1
    else:
        i += 1
    return maxCount

solution(32)