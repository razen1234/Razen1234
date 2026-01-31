class Solution(object):
    def reverseVowels(self, s):
        # Converting s to array
        word = list(s)

        # Creating variables, they'll be our pointers
        start = 0
        end = len(s) - 1

        # all vovels
        vowels = "aeiouAEIOU"

        # Cycle while with two other cycles in it(for two pointers), it will end when start < end
        while start < end:
            # In this cycle pointer "start" will move by 1 after finding vowel
            while start < end and vowels.find(word[start]) == -1:
                start += 1
                
            # In this cycle the procces is same but here we're moving pointer "end" by -1
            while start < end and vowels.find(word[end]) == -1:
                end -= 1

            # Swap the vowels found at the start/end of word to make a word with reversed vowels 
            word[start], word[end] = word[end], word[start]

            # Move the pointers to start the next interaction
            start += 1
            end -= 1

        # returning "" and joining the completed word with reversed vowels
        return "".join(word)
