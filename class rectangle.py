#Артем Трет'яков
class Rectangle:
    """Клас, що представляє прямокутник."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Обчислює площу прямокутника."""
        return self.width * self.height

width = int(input("Ведiть ширину прямокутника: "))
height = int(input("Ведiть висоту прямокутника: "))
rect = Rectangle(width, height)
print(f"Площа прямокутника: {rect.area()}")