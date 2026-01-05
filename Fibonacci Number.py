class Solution:
    def fib(self, n: int) -> int:
        # To find fibonacci number we need to use this formula: F(n) = F(n - 1) + F(n - 2)
        # We have two "ifs" to check if n = 0 or 1, return 0 or 1 because formula won't work with them 
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Making two variables a is previous number: F(n-2), and b is current: F(n-1)
        a = 0
        b = 1
        # cycle for work from 2 because we've already checked 0 and 1
        for i in range(2, n + 1):
            # In this line we calculating fib num with formula
            a, b = b, a + b
        # In the end of cycle current b becomes fibonacci number, so we return it as our answer
        return b
        
