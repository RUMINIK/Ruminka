class Student:
    """Класс для представления студента"""

    def __init__(self, first_name, last_name, patronymic, group, grades):

        if not isinstance(grades, list) or len(grades) != 4:
            raise ValueError("Оценки должны быть списком из 4 элементов")
        if not all(isinstance(g, (int, float)) and 0 <= g <= 100 for g in grades):
            raise ValueError("Оценки должны быть числами от 0 до 100")

        self.first_name = first_name
        self.last_name = last_name  #
        self.patronymic = patronymic
        self.group = group
        self.grades = grades

    def get_average_grade(self):
        """Расчет среднего балла студента"""
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}, Группа: {self.group}"


class StudentManager:
    """Класс для управления данными студентов"""

    def __init__(self):
        self.students = {}
        self.next_id = 1

    def add_student(self, first_name, last_name, patronymic, group, grades):
        """Добавление нового студента"""
        student = Student(first_name, last_name, patronymic, group, grades)
        self.students[self.next_id] = student
        self.next_id += 1
        return self.next_id - 1

    def get_all_students(self):
        """Получение списка всех студентов"""
        return [(id, student) for id, student in self.students.items()]

    def get_student(self, student_id):
        """Получение информации о конкретном студенте"""
        return self.students.get(student_id)

    def update_student(self, student_id, first_name, last_name, patronymic, group, grades):
        """Обновление данных студента"""
        if student_id not in self.students:
            return False
        self.students[student_id] = Student(first_name, last_name, patronymic, group, grades)
        return True

    def delete_student(self, student_id):
        """Удаление студента"""
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False

    def get_group_average(self, group):
        """Расчет среднего балла группы"""
        group_students = [s for s in self.students.values() if s.group == group]
        if not group_students:
            return 0.0
        return sum(s.get_average_grade() for s in group_students) / len(group_students)


def main():
    """Демонстрация работы системы"""
    manager = StudentManager()




    print("=== Добавление студентов ===")
    student1_id = manager.add_student("Иван", "Иванов", "Иванович", "Группа A", [85, 90, 75, 95])
    student2_id = manager.add_student("Петр", "Петров", "Петрович", "Группа A", [70, 85, 90, 80])
    student3_id = manager.add_student("Мария", "Сидорова", "Александровна", "Группа B", [95, 85, 90, 92])
    print("Студенты успешно добавлены")


    print("\n=== Список всех студентов ===")
    for student_id, student in manager.get_all_students():
        print(f"ID: {student_id}, {student}, Средний балл: {student.get_average_grade():.2f}")

    print("\n=== Информация о студенте ===")
    student = manager.get_student(student1_id)
    if student:
        print(f"Студент: {student}")
        print(f"Средний балл: {student.get_average_grade():.2f}")


    print("\n=== Обновление данных студента ===")
    manager.update_student(student1_id, "Иван", "Иванов", "Иванович", "Группа A", [90, 95, 85, 100])
    student = manager.get_student(student1_id)
    print(f"Обновленные данные: {student}, Новый средний балл: {student.get_average_grade():.2f}")

    print("\n=== Средний балл по группам ===")
    print(f"Группа A: {manager.get_group_average('Группа A'):.2f}")
    print(f"Группа B: {manager.get_group_average('Группа B'):.2f}")

    print("\n=== Удаление студента ===")
    if manager.delete_student(student2_id):
        print(f"Студент с ID {student2_id} успешно удален")

    print("\nОставшиеся студенты:")
    for student_id, student in manager.get_all_students():
        print(f"ID: {student_id}, {student}")


if __name__ == "__main__":
    main()
