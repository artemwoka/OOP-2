#Артем Трет'яков
import random
class Pet:
    """Віртуальний вихованець."""

    total = 0
    
    @staticmethod
    def status():
        print("Загальна кількість звірят:", Pet.total)
   
    def __init__(self, name):
        self._name = name
        self.hunger = random.randint(0, 10)
        self.boredom = random.randint(0, 10)
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
        ans += "Голод " + str(self.hunger) + " одиниць \nнудьга " + str(self.boredom) +" одиниць.\n"
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
    list_farm = []
    amout = input("Скільки ви хочете мати звіряток?")
    for i in range(int(amout)):
        
        pet_name = input(f"Як ви назвете {i +1} звірятко? ")
        pet_i = Pet(pet_name)
        list_farm.append(pet_i)
    pet_i = None

    choice = None
    while choice != "0":
        print(
            """
            Моє звірятко

            0 - Вийти
            1 - Дізнатися, про самопочуття звірят
            2 - Покормити звірят
            3 - Пограти з звірятами
            4 - Змінити ім'я звірят
            """
        )

        choice = input("Ваш вибір: ")
        print()

        # вихід
        if choice == "0":
            print("До побачення.")

        elif choice == "1":
            for pet in list_farm:
                pet.talk()


        elif choice == "2":
            food = int(input("Скільки їжі дати звірятamu? "))
            for pet in list_farm:
                pet.eat(food)


        elif choice == "3":
            fun_time = int(input("Скільки часу гратися зі звірятamu? "))
            for pet in list_farm:
                pet.play(fun_time)

        elif choice == "4":
            new_name = input("Введіть нове ім'я: ")
            for pet in list_farm:
                pet.name = new_name
        
        elif choice == "адмін":
            for pet in list_farm:

                print(pet)

        else:
            print("Вибачте, у меню немає пункту", choice)


main()