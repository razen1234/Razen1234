class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # We need to find the difference between two str, so:
        # With cycle for we can take every element and check if it's equal to element from t, if not then return i(that different element) - that's solution
        for e in t:
            if s.count(e) != t.count(e):
                return e
