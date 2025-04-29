class Train:
    def __init__(self, destination, number, departure_time):
        self.destination = destination
        self.number = number
        self.departure_time = departure_time

    def display_info(self):
        print(f"Поезд №{self.number}: {self.destination}, {self.departure_time}")

trains = [
    Train("Москва", 101, "08:00"),
    Train("Санкт-Петербург", 202, "09:30"),
    Train("Казань", 303, "10:15")
]

user_input = input("Введите номер поезда: ")
for train in trains:
    if train.number == int(user_input):
        train.display_info()
        break
else:
    print("Поезд с таким номером не найден.")