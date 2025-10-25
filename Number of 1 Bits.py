class Solution:
    def hammingWeight(self, n: int) -> int:
        #  Переводим n у двійковий рядок за допомогою bin() і рахуєм 1, ну і зразу повертаєм
        return bin(n).count('1')
      #  За bin() я питався у ChatGPT
