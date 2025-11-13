class Solution:
    def countBits(self, n: int) -> List[int]:
        # Creating an list for counting
        count = [0]
        #  Running all nums from 1 to "n"
        for i in range (1, n + 1):
            # [i >> 1] is shifting for 1 bit(this is live diving number by 2 without remainder) and i % 2 is the last digit in binary notation
            count.append(count[i >> 1] + i % 2)
        # Return an answer
        return count
