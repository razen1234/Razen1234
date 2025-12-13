class Solution:
    def moveZeroes(self, nums):
        # Create pointer for two pointers system
        j = 0
        # Cycle for with range of list "nums"
        for i in range(len(nums)):
            # Working only with non zero numbers
            if nums[i] != 0:
                # Swap current element and j with places 
                nums[i], nums[j] = nums[j], nums[i]
                # Move j forward by 1 for another element which isn't zero
                j += 1
