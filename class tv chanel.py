class TV:
    """Клас для моделювання телевізора з каналами та гучністю."""
    def __init__(self, brand, min_channel=1, max_channel=100, min_volume=0, max_volume=50):
        self.min_channel = min_channel
        self.max_channel = max_channel
        self.current_channel = min_channel
        self.min_volume = min_volume
        self.max_volume = max_volume
        self.volume = (min_volume + max_volume) // 2
        self.brand = brand
    
    def set_channel(self, channel):
        """Встановлює поточний канал, якщо він у допустимому діапазоні."""
        if self.min_channel <= channel <= self.max_channel:
            self.current_channel = channel
        else:
            print(f"Канал {channel} недоступний. Виберіть канал від {self.min_channel} до {self.max_channel}.")
    def increase_volume(self):
        """Збільшує гучність на 1, якщо не досягнуто максимального рівня."""
        if self.volume < self.max_volume:
            self.volume += 1
            print(f"Гучність: {self.volume}")
        else:
            print("Гучність вже на максимальному рівні.")
    def decrease_volume(self):
        """Зменшує гучність на 1, якщо не досягнуто мінімального рівня."""
        if self.volume > self.min_volume:
            self.volume -= 1
            print(f"Гучність: {self.volume}")
        else:
            print("Гучність вже на мінімальному рівні.")

    def __str__(self):
        """Повертає рядкове представлення об'єкта телевізора."""
        return f"Телевізор - Канал: {self.current_channel}, Гучність: {self.current_volume}"
def main():
    tv = TV("Samsung")
    choice = None

    while choice != 0:
        print(" Меню телевізора:")
        print("1. Встановити канал")
        print("2. Збільшити гучність")
        print("3. Зменшити гучність")
        print("0. Вийти")
        choice = int(input("Виберіть опцію: "))

        if choice == 1:
            try:
                channel = int(input(f"Введіть канал ({tv.min_channel}-{tv.max_channel}): "))
                tv.set_channel(channel)
            except ValueError:
                print("Будь ласка, введіть дійсне число для каналу.")
        elif choice == 2:
            tv.increase_volume()
        elif choice == 3:
            tv.decrease_volume()
        elif choice == 0:
            print("Вихід з програми.")
        else:
            print("Такої опції немає. Спробуйте ще раз.")
main()






