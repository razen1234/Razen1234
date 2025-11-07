class Solution:
    def addDigits(self, num: int) -> int:
        # return 0 if num is 0, because formula don't work on 0, but answer will be 0
        if num == 0:
            return 0
        # We're returning 9, because if "num % 9 == 0" it means that 9 is a root of the num and it's can be divided by 9 (Example: 18 = 1+8=9, 18%9=0)
        if num % 9 == 0:
            return 9
        # Else return that (17 % 9 = 8)
        else:
            return (num % 9)
