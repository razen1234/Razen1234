class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Creating two variable as pointers to count duplicates and numbers witnout them
        no_dupl = 0 
        dupl = 1
        # Cycle "while" will only work in list "nums" 
        while dupl in range(len(nums)):
            # If numbers are same count it in "dupl"
            if nums[no_dupl] == nums[dupl]:
                dupl += 1
            else:
                # If they're not same, write it in "no_dupl"
                nums[no_dupl+1] = nums[dupl]
                # Move forward both variable
                no_dupl += 1
                dupl += 1
        # return answer(+1 because indexing)
        return no_dupl + 1 
