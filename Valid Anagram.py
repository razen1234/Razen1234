class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Cheking if s and t have same amount of characters 
        if len(s) != len(t):
            return False
        # Creating array, based on english alphabet of 26 characters
        array = [0] * 26
        # Cycle for in range of "s"
        for i in range(len(s)):
            # Ord represents nuber of character position in characters set, with every loop we increment for s and decrement for t
            array[ord(s[i]) - ord("a")] += 1
            array[ord(t[i]) - ord("a")] -= 1
        # Cheking if all counts equal to zero 
        for check in array:
            if check != 0:
                return False
        # Return True if they are
        return True
