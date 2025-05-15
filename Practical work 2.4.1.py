import sqlite3

class Student:
    """Класс для представления студента"""

    def __init__(self, first_name, last_name, patronymic, group, grades):
        if not isinstance(grades, list) or len(grades) != 4:
            raise ValueError("Оценки должны быть списком из 4 элементов")
        if not all(isinstance(g, (int, float)) and 0 <= g <= 100 for g in grades):
            raise ValueError("Оценки должны быть числами от 0 до 100")
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.group = group
        self.grades = grades

    def get_average_grade(self):
        """Расчет среднего балла студента"""
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}, Группа: {self.group}"

class StudentManager:
    """Класс для управления данными студентов с использованием базы данных"""

    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Создание таблицы студентов при необходимости"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                patronymic TEXT,
                group_name TEXT,
                grades TEXT -- храним оценки как строку JSON или разделённые запятыми
            )
        ''')
        self.conn.commit()

    def add_student(self, first_name, last_name, patronymic, group, grades):
        """Добавление нового студента в базу"""
        import json
        grades_str = json.dumps(grades)
        self.cursor.execute('''
            INSERT INTO students (first_name, last_name, patronymic, group_name, grades)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, patronymic, group, grades_str))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_students(self):
        """Получение всех студентов из базы"""
        import json
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            student_id = row[0]
            first_name = row[1]
            last_name = row[2]
            patronymic = row[3]
            group = row[4]
            grades = json.loads(row[5])
            student_obj = Student(first_name, last_name, patronymic, group, grades)
            result.append((student_id, student_obj))
        return result

    def get_student(self, student_id):
        """Получение информации о конкретном студенте"""
        import json
        self.cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
        row = self.cursor.fetchone()
        if row:
            first_name = row[1]
            last_name = row[2]
            patronymic = row[3]
            group = row[4]
            grades = json.loads(row[5])
            return Student(first_name, last_name, patronymic, group, grades)
        return None

    def update_student(self, student_id, first_name, last_name, patronymic, group, grades):
        """Обновление данных студента"""
        import json
        if not self.get_student(student_id):
            return False
        grades_str = json.dumps(grades)
        self.cursor.execute('''
            UPDATE students SET first_name=?, last_name=?, patronymic=?, group_name=?, grades=?
            WHERE id=?
        ''', (first_name, last_name, patronymic, group, grades_str, student_id))
        self.conn.commit()
        return True

    def delete_student(self, student_id):
        """Удаление студента"""
        self.cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        self.conn.commit()
        return True

    def get_group_average(self, group):
        """Расчет среднего балла группы"""
        import json
        self.cursor.execute('SELECT grades FROM students WHERE group_name=?', (group,))
        
        rows = self.cursor.fetchall()
        
        total_grades = []
        
        for (grades_str,) in rows:
            grades = json.loads(grades_str)
            total_grades.extend(grades)
        
        if not total_grades:
            return 0.0
        
        return sum(total_grades) / len(total_grades)

    def close(self):
       """Закрытие соединения с базой"""
       self.conn.close()


def main():
    """Демонстрация работы системы с базой данных"""
    manager = StudentManager()

    print("=== Добавление студентов ===")
    student1_id = manager.add_student("Иван", "Иванов", "Иванович", "Группа A", [85, 90, 75 ,95])
    student2_id = manager.add_student("Петр", "Петров", "Петрович", "Группа A", [70 ,85 ,90 ,80])
    student3_id = manager.add_student("Мария", "Сидорова", "Александровна", "Группа B", [95 ,85 ,90 ,92])
    print("Студенты успешно добавлены")

    print("\n=== Список всех студентов ===")
    for student_id ,student in manager.get_all_students():
       print(f"ID: {student_id}, {student}, Средний балл: {student.get_average_grade():.2f}")

    print("\n=== Информация о студенте ===")
    student = manager.get_student(student1_id)
    if student:
       print(f"Студент: {student}")
       print(f"Средний балл: {student.get_average_grade():.2f}")

    print("\n=== Обновление данных студента ===")
    manager.update_student(student1_id,"Иван","Иванов","Иванович","Группа A",[90 ,95 ,85 ,100])
    student=manager.get_student(student1_id)
    print(f"Обновленные данные: {student}, Новый средний балл: {student.get_average_grade():.2f}")

    print("\n=== Средний балл по группам ===")
    print(f"Группа A: {manager.get_group_average('Группа A'):.2f}")
    print(f"Группа B: {manager.get_group_average('Группа B'):.2f}")

    print("\n=== Удаление студента ===")
    if manager.delete_student(student2_id):
       print(f"Студент с ID {student2_id} успешно удален")

    print("\nОставшиеся студенты:")
    for student_id ,student in manager.get_all_students():
       print(f"ID: {student_id}, {student}")

    # Не забудьте закрыть соединение при завершении работы
    manager.close()

if __name__ == "__main__":
   main()
