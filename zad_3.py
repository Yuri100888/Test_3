# Класс Alphabet
# 1) Создайте класс Alphabet
# 2) Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1)lang - язык и 2)letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3) Создайте метод print(), который выведет в консоль буквы алфавита
# 4) Создайте метод letters_num(), который вернет количество букв в алфавите

# Класс EngAlphabet
# 1) Создайте класс EngAlphabet путем наследования от класса Alphabe
# 2) Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначения языка (например 'En') и строка, состоящая из всех букв
# алфавита (можно воспользоваться свойством ascii_uppercase из модуля string).
# 3) Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите
# 4) Создайте метод is_en_letter(), который будет принимать букв в качестве параметра и определять,
# относится ли эта буква к англййскому алфавиту
# 5) Переопределите метод letters_num() - пуст в текущем классе он будет возвращать значение свойства __letters_num
# 6) Создайте статический метод example(), который будет возвращать пример текста на английском языке


# Создайте объект класса EngAlphabet
# Напечатайте буквы алфавита для этого объекта
# Выведите количтсво букв в алфавите
# Проверьте, относится ли буква F к англйскому алфавиту
# Проверьте, относиться ли буква Щ к английскому алфавиту
# Выведите пример текста на английском языке
from string import ascii_uppercase


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__(lang='En', letters=ascii_uppercase)

    def is_en_letter(self, letter):
        if str(letter).upper() in self.letters:
            print(f'Буква {letter} относится к английскому алфавиту')
        else:
            print(f'Буква {letter} не относится к английскому алфавиту')

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return ('This is an example text in English')


#
#
if __name__ == '__main__':
    alphabet_eng = EngAlphabet()
    alphabet_eng.print()
    print(alphabet_eng.letters_num())
    alphabet_eng.is_en_letter('F')
    alphabet_eng.is_en_letter('Щ')
    print(alphabet_eng.example())
