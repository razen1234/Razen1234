class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Creating an empty varialbe
        previous = None
        # Creating "current" as the head of the list
        current = head
        # Cycle "while" will end when "current" will be empty
        while current:
            # Saving next element in variable "temp"
            temp = current.next
            # Reverse the "pointer"; For example: (1 -> 2, None <- 1)
            current.next = previous
            # Saving current element in "previous"
            previous = current
            # Move "current" to next element
            current = temp
        # Returning answer(previos is now a new, reversed list)
        return previous
