class Animals:
    name = None
    weight = None  # масса
    produce_a_product = None  # производимый продукт
    growth_factor = None  # Коэффициент роста

    def __init__(self, weight, produce_a_product, growth_factor):
        self.weight = weight
        self.produce_a_product = produce_a_product
        self.growth_factor = growth_factor
        print("Экземпляр класс создан")

    def graze(self, value):  # фунция пастись value дней
        print("Животное отправили пастись и наращивать массу")
        self.weight += value * self.growth_factor
        print("Масса: {} кг".format(self.weight))

    def description_animals(self):
        print("Животное {} массой {} кг., дает продукт {} с коэфф. роста {} кг в день".format(self.name, self.weight,
                                                                                              self.produce_a_product,
                                                                                              self.growth_factor))


# Класс парнокопытнах для Коровы, козы, овцы, свиньи
class Artiodactyl(Animals):
    def graze(self, value):
        self.growth_factor += 2  # Для парнокопытных коэффициент роста +2
        print("Удар копытом")
        super().graze(value)


# Класс коровы на основе класса парнокопытных
class Cow(Artiodactyl):
    name = "Корова"

    def graze(self, value):
        print("Муууу")
        super().graze(value)


# Класс козы на основе класса парнокопытных
class Goat(Artiodactyl):
    name = "Коза"

    def graze(self, value):
        print("Бееееееее")
        super().graze(value)


# Класс овцы на основе класса парнокопытных
class Sheep(Artiodactyl):
    name = "Овца"

    def graze(self, value):
        print("Меееее")
        super().graze(value)


# Класс свиньи на основе класса парнокопытных
class Pig(Artiodactyl):
    name = "Свинья"

    def graze(self, value):
        self.growth_factor += 10  # Для свиней коэффициент роста +10
        print("Хрюююю")
        super().graze(value)


# Класс птиц для Утки, куры, гуси
class Birds(Animals):
    def graze(self, value):
        print("Взмах крылом")
        super().graze(value)

    def fly(self, value):
        print("Полет на расстояние:{} метров".format(value))


class Duck(Birds):
    name = "Утка"

    def graze(self, value):
        print("Кряяя Кряяя")
        super().graze(value)


class Chicken(Birds):
    name = "Курица"

    def graze(self, value):
        print("Кукареку")
        super().graze(value)


class Goose(Birds):
    name = "Гусь"

    def graze(self, value):
        print("Гагагага")
        super().graze(value)


pig1 = Pig(300, "Мясо", 3)
pig1.description_animals()
pig1.graze(3)
pig1.description_animals()

cow1 = Cow(500, "Молоко", 2)
cow1.description_animals()
cow1.graze(3)
cow1.description_animals()

goat1 = Goat(46, "Молоко", 1)
goat1.description_animals()
goat1.graze(3)
goat1.description_animals()

sheep1 = Sheep(33, "Молоко", 1)
sheep1.description_animals()
sheep1.graze(3)
sheep1.description_animals()

duck1 = Duck(10, "Мясо", 1)
duck1.description_animals()
duck1.graze(3)
duck1.description_animals()

chicken1 = Chicken(7, "Яйцо", 1)
chicken1.description_animals()
chicken1.graze(3)
chicken1.description_animals()

goose1 = Goose(15, "Мясо", 1)
goose1.description_animals()
goose1.graze(3)
goose1.description_animals()
