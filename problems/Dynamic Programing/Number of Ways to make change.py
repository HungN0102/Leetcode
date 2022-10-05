def numberOfWaysToMakeChange(n, denoms, memo={}):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    if n < 0:
        return 0

    totalCount = 0
    for i in range(len(denoms)):
        totalCount += numberOfWaysToMakeChange(n-denoms[i], denoms[i:],memo)

    memo[n] = totalCount
    return totalCount