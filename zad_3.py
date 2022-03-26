# Создайте объект класса EngAlphabet
# Напечатайте буквы алфавита для этого объекта
# Выведите количтсво букв в алфавите
# Проверьте, относится ли буква F к англйскому алфавиту
# Проверьте, относиться ли буква Щ к английскому алфавиту
# Выведите пример текста на английском языке
from string import ascii_uppercase


class EngAlphabet:
    alphabet = ascii_uppercase

    def len_alphabet(self):
        print(len(self.alphabet))

    def is_this_letter_in_English(self, letter):
        if str(letter).upper() in self.alphabet:
            print(f'Буква {letter} относится к английскому алфавиту')
        else:
            print(f'Буква {letter} не относится к английскому алфавиту')

    @staticmethod
    def example():
        print('This is an example text in English')


if __name__ == '__main__':
    alphabet_eng = EngAlphabet()
    alphabet_eng.len_alphabet()
    alphabet_eng.is_this_letter_in_English('F')
    alphabet_eng.is_this_letter_in_English('Щ')
    EngAlphabet.example()
