class Solution:
  # Початок функції
    def plusOne(self, digits: List[int]) -> List[int]:
      # Цикл for, який працює зі списком(і його довжиною) digits, перше значення: звідки починаємо, друге де закінчуємо, третє: крок
        for i in range(len(digits) - 1, -1, -1):
          # Якщо число не дорівнює 9, додаєм 1
            if digits[i] != 9:
                digits[i] += 1
              # Повертаєм значення
                return digits
              # Якщо число = 9 міняєм на 0 
            digits[i] = 0
          # На початок списку додаєм 1 і повертаєм значення
        return [1] + digits
