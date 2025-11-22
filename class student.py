#Артем Трет'яков
class Student:
    """Клас студент з ім'ям та оцінками"""
    def __init__(self, name, grades):
        """Ініціалізація студента з ім'ям та оцінками."""
        self.name = name
        list(self.grades) = grades
    def average_grade (self):
        """Обчислює середню оцінку студента."""
        if len(self.grades) == 0:
            return "Немає оцінок для обчислення середньої."
        else:
            return sum(self.grades) / len(self.grades) 
def main():    
    name = input("Введіть ім'я студента: ")
    grades_input = input("Введіть оцінки студента через пробіл: ")
    grades = list(map(int, grades_input.split()))
    student = Student(name, grades)
    print(f"Середня оцінка студента {student.name}: {student.average_grade():.2f}")

main()