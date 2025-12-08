class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Creating list 
        answer = []
        # Working in range of n and adding + 1 to range
        for i in range(1, n + 1):
            # So if we have i % 3 == 0 we replace number with "Fizz"; if we have i % 5 == 0 we replace with "Buzz"; and same thing but with two correct condition we will append "FizzBuzz". All of that just in "if - elif - else" system. 
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        # Returning answer
        return answer
