# Импортируем функцию стандартного модуля random.
from random import randint

# Вот она — новая глобальная константа.
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'  # Описание
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Константа для диапазона очков защиты.
    RANGE_VALUE_DEFENCE = (1, 5)

    SPECIAL_BUFF = 15  # Значение очков урона из Special (константа)
    SPECIAL_SKILL = 'Удача'  # Название умения из Special (константа)

    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки
    def attack(self):

        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    # Объявляем метод защиты.
    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        return (f'{self.name} применил специальное умение ')
        f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".'

    # Вывод названия и описания.
    # Метод __str__ возвращает имя класса и описание класса.
    # Вывести имя у объекта класса - использовать атрибут __class__.__name__
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


# Cоздаем объект (атрибут) класса Warrior с именем "Кодослав".
# Передали атрибут Warrior в переменную.
warrior = Warrior('Кодослав')
# Dызывается метод __str__, который выводит название класса и
# описание персонажа.
print(warrior)
# Вызывается метод attack объекта warrior, который возвращает строку,
# представляющую собой результат атаки воина.
print(warrior.attack())
