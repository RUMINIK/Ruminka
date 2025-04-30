class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):
        """Метод для расчета и вывода зарплаты работника."""
        salary = self.rate * self.days
        print(f"Зарплата работника {self.name} {self.surname}: {salary} у.е.")
worker1 = Worker("Иван", "Иванов", 100, 20)
worker1.get_salary()
