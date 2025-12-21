class Solution:
    def strStr(self, haystack, needle):
        # Cycle for will only start if length of haystack is bigger than needle
        for i in range(len(haystack) - len(needle) + 1):
            # Return i if part of haystack(equal in length to needle) equal to needle itself
            if haystack[i : i + len(needle)] == needle:
                return i
        # If cycle didn't started return -1 because needle is bigger        
        return -1
