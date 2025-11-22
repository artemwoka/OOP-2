
class Pet:
    """Віртуальний вихованець."""

    total = 0
    
    @staticmethod
    def status():
        print("Загальна кількість звірят:", Pet.total)
   
    def __init__(self, name, hunger=0, boredom=0):
        self._name = name
        self.hunger = hunger
        self.boredom = boredom
        Pet.total += 1
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Ім'я не може бути порожнім рядком.")
        else:
            self._name = new_name
            print("Ім'я змінено на", self._name)


    def talk(self):
        print("Меня звати", self._name,
              ", і зараз я почуваюся", self.mood)
        self._pass_time()
        
    def eat(self, food):
        print("Ммм... Дякую!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self._pass_time()

    def play(self, fun):
        print("Уiiii")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self._pass_time()

    def __str__(self):
        ans = "Об'єкт класу Pet\n"
        ans += "Ім'я: " + self.name + "\n"
        return ans
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "непогано"
        elif 11 <= unhappiness <= 15:
            m = "не сказати що добре"
        else:
            m = "жахливо"
        return m
    def _pass_time(self):
        self.hunger += 1
        self.boredom += 1


def main():

    pet_name = input("Як ви назвете своє звірятко? ")
    pet = Pet(pet_name)

    choice = None
    while choice != "0":
        print(
            """
            Моє звірятко

            0 - Вийти
            1 - Дізнатися, про самопочуття звірятка
            2 - Покормити вихованця
            3 - Пограти з вихованцем
            4 - Змінити ім'я вихованця
            """
        )

        choice = input("Ваш вибір: ")
        print()

        # вихід
        if choice == "0":
            print("До побачення.")

        elif choice == "1":
            pet.talk()

        elif choice == "2":
            food = int(input("Скільки їжі дати звірятку? "))
            pet.eat(food)

        elif choice == "3":
            fun_time = int(input("Скільки часу гратися зі звірятком? "))
            pet.play(fun_time)

        elif choice == "4":
            new_name = input("Введіть нове ім'я: ")
            pet.name = new_name

        else:
            print("Вибачте, у меню немає пункту", choice)


main()