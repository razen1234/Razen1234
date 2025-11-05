class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Creating "index" for counting nums, which aren't equal val
        index = 0
        #Cycle for, which works with every element in list "nums"
        for i in range(len(nums)):
            # If elemet in list isn't equal to val
            if nums[i] != val:
                # Replacing element(i) in "nums" to index 
                nums[index] = nums[i]\
                # Count + number, which isn't equal val
                index += 1 
        # Return result
        return index
