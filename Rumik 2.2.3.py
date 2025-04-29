class NumberPair:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print(f"Числа: {self.num1}, {self.num2}")

    def change_numbers(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def max_value(self):
        return max(self.num1, self.num2)

pair = NumberPair(5, 10)
pair.display()

print("Сумма:", pair.sum())
print("Наибольшее значение:", pair.max_value())


pair.change_numbers(20, 15)
pair.display()

print("Сумма после изменения:", pair.sum())
print("Наибольшее значение после изменения:", pair.max_value())