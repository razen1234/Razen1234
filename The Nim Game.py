class Solution:
    def canWinNim(self, n: int) -> bool:
        # Description: The Nim game it's game where you and your friend have 4 stones, you can take from 1 to 3 stones, the one who pulls the last stone wins, so if your move is first then you'll lose. 
        # This pattern works even when number is bigger, example:(8, 12, 16...), but if number doesn't divides by 4 without remainder, your friend will lose. So we've just tested if number can be divided by 4.
        return n % 4 != 0
