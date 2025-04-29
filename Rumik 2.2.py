class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades  

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date

    def change_group_number(self, new_group_number):
        self.group_number = new_group_number

    def display_info(self):
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.birth_date}")
        print(f"Номер группы: {self.group_number}")
        print(f"Успеваемость: {self.grades}")

def find_student(students, surname, birth_date):
    for student in students:
        if student.surname == surname and student.birth_date == birth_date:
            return student
    return None


if __name__ == "__main__":

    students = [
        Student("Иванов", "2000-01-15", "101", [5, 4, 3, 4, 5]),
        Student("Петров", "1999-12-20", "102", [4, 4, 4, 4, 4]),
        Student("Сидоров", "2001-03-10", "103", [3, 5, 2, 4, 3])
    ]


    students[0].change_surname("Иванович")
    students[1].change_birth_date("1999-12-21")
    students[2].change_group_number("104")


    search_surname = input("Введите фамилию студента: ")
    search_birth_date = input("Введите дату рождения студента (ГГГГ-ММ-ДД): ")

    found_student = find_student(students, search_surname, search_birth_date)
    if found_student:
        found_student.display_info()
    else:
        print("Студент не найден.")
