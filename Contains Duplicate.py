class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the list for better operating with it
        nums.sort()
        # Cycle "for" in range of list "nums"
        for i in range(1, len(nums)):
            # If our next number equal to previuos, then it means list have duplicates(example: nums[i] = 3, nums[i - 1] = 3; 3 == 3)
            if nums[i] == nums[i - 1]:
                return True
            # Return False if list don't have any duplicates 
        return False
