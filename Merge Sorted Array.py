class Solution:
    def merge(self, nums_1: List[int], m: int, nums_2: List[int], n: int) -> None:
        # Expalanation: we have two arrays(lists), first with "m" and second with "n", we will work on second list(nums_2) with "n" by running every element in it
        for i in range(n):
            # We will add every new element from nums_2 to the end of list nums_1
            nums_1[m+i] = nums_2[i]
        # Sorting united list with method sort()
        nums_1.sort()
