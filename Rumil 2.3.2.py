class Worker:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

worker = Worker("Маринадзе", "Программист", 100000)

print(worker.get_name())
print(worker.get_position())
print(worker.get_salary())