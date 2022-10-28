# def decodeWays(number):
#     return solveDP(str(number), 0)

# def solveDP(number, index):
#     if index == len(number):
#         return 1
#     if number[index] == "0":
#         return 0


#     result = solveDP(number, index+1)
#     if int(number[index:index+2]) <= 26 and index + 2 <= len(number):
#         result += solveDP(number, index+2)

#     return result

# decodeWays(111111111111111111111111111111111111111111111)


A = 1
B = 2

C = A
A = B
B = C