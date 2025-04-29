class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1
counter = Counter()
print("Начальное значение:", counter.value)

counter.increment()
print("После увеличения:", counter.value)

counter.decrement()
print("После уменьшения:", counter.value)

custom_counter = Counter(5)
print("Начальное значение (пользовательское):", custom_counter.value)

custom_counter.increment()
print("После увеличения (пользовательское):", custom_counter.value)

custom_counter.decrement()
print("После уменьшения (пользовательское):", custom_counter.value)