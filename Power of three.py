class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # If number is equal or lower than 0, return False because there can't be 3^x = 0 or 3^x = -1
        if n <= 0:
            return False
        # Will work while number is divisible by 3
        while n % 3 == 0:
            # Here n is being divided by 3(example: 27 // 3 = 9 -> 9 // 3 = 3 -> 3 // 3 = 1)
            n //= 3
        # After loops in while cycle we're checking if n == 1, if it is then we return answer
        return n == 1
