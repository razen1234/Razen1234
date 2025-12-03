class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        # Creating variables for range of Binary search
        left = 2
        right = num // 2
        # Cycle will end if left is bigger than right
        while left <= right:
            # Finding mid number
            mid = (left + right) // 2
            # Finding squared mid
            squared = mid * mid
            # If mid in square = num return true as an answear
            if squared == num:
                return True
            # If not first condition then change left to mid + 1
            elif squared < num:
                left = mid + 1
            # Else change right to mid - 1
            else:
                right = mid - 1
        # In anohter way return False
        return False
