class Solution:
    def mySqrt(self, x: int) -> int:
        # Self explanatory: If our number is 0 return 0
        if x == 0:
            return 0
        # creating variables for measuring range of nums we are working with
        first_num = 1
        last_num = x
        # Cycle will last until "first_num" is bigger than "last_num"
        while first_num <= last_num:
            # Finding "middle" number of a range
            mid = first_num + (last_num - first_num) // 2
            # Returnig mid if x divided by mid (exmple: 16 / 4 = 4; 4 * 4 = 16; return 4) 
            if mid == x // mid:
                return mid
            # If mid is bigger than update last_num with mid - 1
            elif mid > x // mid:
                last_num = mid - 1
            # In another conditions update first_num with mid + 1
            else:
                first_num = mid + 1
        # Return last
        return last_num
