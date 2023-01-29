class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.list_grades= []


    def grade_new(self, lecturer, course, grade): #выставление оценки лектору
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade in range(1,11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_student(self):
        if not self.grades:
            return 0
        list_grades = []
        for new in self.grades.values():
            list_grades.extend(new)
        return round(sum(list_grades) / len(list_grades), 2)

    def __str__(self) -> str:
        return f" Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {self.average_student()} \n" \
               f"Курсы в процессе изучения: {self.courses_in_progress} \n" \
               f"Завершенные курсы: {self.finished_courses} \n"

    def __le__(self, other: "Student") -> bool:
        return self.average_student() <= other.average_student()

    def __eq__(self, other: "Student") -> bool:
        return self.average_student() == other.average_student()

    def __lt__(self, other: "Student") -> bool:
        return self.average_student() < other.average_student()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.grades = {}

    def rating(self): #рейтинг лекторов
        if not self.grades:
            return 0
        list_grades = []
        for new in self.grades.values():
            list_grades.extend(new)
        return round(sum(list_grades) / len(list_grades), 2)


    def __str__(self) -> str:
        return f" Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self.rating()}"

    def __eq__(self, other: "Lecturer") -> bool:
        return self.rating() == other.rating()

    def __lt__(self, other: "Lecturer") -> bool:
        return self.rating() < other.rating()

    def __le__(self, other: "Lecturer") -> bool:
        return self.rating() <= other.rating()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade): #выставление оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade in range(1,11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f" Имя: {self.name} \n" \
               f"Фамилия: {self.surname}"


#список студентов
student_1 = Student('Алиса', 'Пирст')
student_2 = Student('Майкл', 'Каунр')
#курсы студентов
student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['Git']
student_2.courses_in_progress += ['JavaScript']
student_2.courses_in_progress += ['Go']
student_1.finished_courses += ['C++']
student_2.finished_courses += ['Python']
#Лекторы
lecturer_1 = Lecturer('Клара', 'Унсдей')
lecturer_2 = Lecturer('Том', 'Шомп')
#Список курсов
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_attached += ['Go']
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['JavaScript']
#Проверяющие
reviewer_1 = Reviewer('Остин', 'Лоэнс')
reviewer_2 = Reviewer('Джулия', 'Боти')
#Список курсов
reviewer_1.courses_attached += ['Git']
reviewer_1.courses_attached += ['Go']
reviewer_2.courses_attached += ['Java']
reviewer_2.courses_attached += ['JavaScript']
#оценки лекторам
student_1.grade_new(lecturer_1, 'Git', 7)
student_1.grade_new(lecturer_1, 'Go', 8)
student_1.grade_new(lecturer_2, 'JavaScript', 10)
student_1.grade_new(lecturer_2, 'Java', 5)
student_2.grade_new(lecturer_1, 'Go', 6)
student_2.grade_new(lecturer_1, 'Git', 5)
student_2.grade_new(lecturer_2, 'JavaScript', 9)
student_2.grade_new(lecturer_2, 'Java', 8)

#оценки студентам
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'С++', 8)
reviewer_1.rate_hw(student_2, 'Go', 5)
reviewer_1.rate_hw(student_2, 'JavaScript', 6)
reviewer_2.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Go', 9)

print(f"Первый студент\n{student_1}")
print(f"Второй студент\n{student_2}")
print(f"Первый лектор\n{lecturer_1}\n")
print(f"Второй лектор\n{lecturer_2}\n")
print(f"Первый проверяющий\n{reviewer_1}\n")
print(f"Второй проверябщий\n{reviewer_2}\n")

all_students = [student_1, student_2]
all_lecturers = [lecturer_1, lecturer_2]
all_courses = input('Введите название курса: ')


def compare_students(all_students, all_courses):
    grades_list = []
    for nil in all_students:
        grades_list.extend(nil.grades.get(all_courses, []))
    if not grades_list:
        return "По этому курсу нет оценок"
    return round(sum(grades_list) / len(grades_list), 2)


def compare_lecturers(all_lecturer, all_courses):
  return compare_students(all_lecturer, all_courses)

  print(f'Сравнения всех студентов по средним оценкам за домашние задания: '
      f'{student_1.name} {student_1.surname} {"<" if student_1 < student_2 else (">" if student_1 > student_2 else "=")} {student_2.name} {student_2.surname}')


print(f'Сравнение всех лекторов по средним оценкам за лекции: '
      f'{lecturer_1.name} {lecturer_1.surname} {"<" if lecturer_1 < lecturer_2  else (">" if lecturer_1 > lecturer_2 else "=")} {lecturer_2.name} {lecturer_2.surname}')


print(f"Средняя оценка для всех студентов по курсу {all_courses}: {compare_students(all_students, all_courses)}")


print(f"Средняя оценка для всех лекторов по курсу {all_courses}: {compare_lecturers(all_lecturers, all_courses)}")


