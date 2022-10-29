# 2
def solution(x,y,z):
    print(x+y+z)
    
# 3
def solution(score1, score2):
    print(abs(score1-score2))
    
# 4
def solution(number1, number2):
    if number2 < number1:
        print(number1)
    else:
        print(number2)
        
# 5
for number in range(99,0,-1):
    if number % 2 == 1:
        print(number)
        
# 6
def solution(numbers):
    maxEven = -float("inf")
    maxOdd = -float("inf")

    for num in numbers:
        if num % 2 == 0:
            maxEven = max(maxEven, num)
        else:
            maxOdd = max(maxOdd, num)

    print(maxEven+maxOdd)

# 7
def solution(D, S):
    hashmap = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }
    return (D * hashmap[S])

# 8

def solution(N):
    nineTimes = N // 9
    oneTime = N - 9*nineTimes
    return int(str(oneTime) + str(9)*nineTimes)