class Footballer:
    """Клас, що представляє футболіста"""
    def __init__(self, name, position):
        """
        Конструктор класу Footballer.
        :param name: Ім'я футболіста
        :param position: Позиція футболіста на полі
        """
        self.name = name
        self.position = position

    def __str__(self):
        """Повертає рядкове представлення об'єкта"""
        return f"Футболіст: {self.name}, Позиція: {self.position}"

def create_team():
    """Створює та повертає список футболістів"""
    players_data = [
        ("Андрій Лунін", "Воротар"),
        ("Віталій Миколенко", "Захисник"),
        ("Ілля Забарний", "Захисник"),
        ("Микола Матвієнко", "Захисник"),
        ("Юхим Конопля", "Захисник"),
        ("Тарас Степаненко", "Півзахисник"),
        ("Олександр Зінченко", "Півзахисник"),
        ("Георгій Судаков", "Півзахисник"),
        ("Михайло Мудрик", "Нападник"),
        ("Віктор Циганков", "Нападник"),
        ("Артем Довбик", "Нападник")
    ]
    
    team = []
    for name, position in players_data:
        player = Footballer(name, position)
        team.append(player)
    return team

def main():
    """Основна функція програми"""
    my_team = create_team()
    
    print("Склад футбольної команди:")
    for player in my_team:
        print(player)

main()