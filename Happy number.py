class Solution:
    def isHappy(self, n: int) -> bool:
        # Description to task: Happy number is positive integer, which replaces by squares of its digits until a loop ends with 1, if it doesn't then it isn't a Happy number. Example: 19
#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1
       # If 1 or 7 is our number then return true because they're Happy
        if n == 1 or n == 7:
            return True
       # Every other number which is lower than 10, doesn't equal 1(not happy)
        elif n < 10:
            return False
       # If both conditions don't suit number 
        else:
            # creating sum
            sum = 0
            # Cycle while until n is < 0
            while n > 0:
                # Creating temp, remainder of n goes into temp 
                temp = n % 10
                # Calculating sum with squares of digits: The same exact "Happy" process mentioned earlier
                sum += temp * temp
                # "Cutting" the right side of number: 19 // 10 = 1, and after that 1 // 10 = 0 - cycle ends.
                n = n // 10
            # Rechecking if number is happy and returning the answer 
            return self.isHappy(sum)
