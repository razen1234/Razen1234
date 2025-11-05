class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Variable for counting how many times elements appear in list "nums"
        count = 0
        # "e" stands for element, which will have majority
        e = 0
        # Cycle for, which checks every element in list
        for num in nums:
            # if sum of places in list is equal
            if count == 0:
                # choosing element for majority
                e= num
                # adding "place" to element
                count = 1
                # If that's same elemnt add another place
            elif e == num:
                count += 1
                # If that's not same elemnt minus one place
            else:
                count -= 1
        # Return major element in list(Result)
        return e
