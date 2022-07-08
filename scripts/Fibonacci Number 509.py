class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        
        sequence = [0,1]
        for i in range(2,n+1):
            value = sequence[i-1] + sequence[i-2]
            sequence.append(value)
            
        return sequence[n]