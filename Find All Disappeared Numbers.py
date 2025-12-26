class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Saving lengh of list in "n"
        n = len(nums)
        # Cycle for in range of nums
        for i in range(n):
            # With cycle while we are moving digit to equal index, it will run until every number will de moved
            while nums[i] != nums[nums[i] - 1]:
                # Swaping indexes
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # Crearing result
        result = []
        # With cycle for, filling result
        for i in range(n):
            # If element isn't equal to i + 1, then append to result because it's of the missing numbers
            if nums[i] != i + 1:
                result.append(i + 1)
        # returning answer
        return result
