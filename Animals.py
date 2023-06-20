"""
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
"""

"""
5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.

"""


class Animals:

    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f"{self.name} {self.weight} {self.age}"


class Bird(Animals):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "Летает"

    def say(self):
        return self._sound

    def __str__(self):
        return f"{super().__str__()} {self.bird_type} {self.move()} {self.say()}"


class Dog(Animals):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type
        self.commands = []

    def move(self):
        return "Бегает"

    def say(self):
        return "Гав-гав"

    def __str__(self):
        return f"{super().__str__()} {self.dog_type} {self.move()} {self.say()}"


class Fish(Animals):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "Плавает"

    def say(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.fish_type} {self.move()}"


dog = Dog("Рэкс", 40, 5, "Такса")
bird = Bird("Гоша", 1, 3, "Попугай", "Чирик")
fish = Fish("Карп", 10, 5, "Речной")

print(dog)
print(bird)
print(fish)