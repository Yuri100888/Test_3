# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card(numb_card=input('Введите номер карты: ')):
    if len(numb_card) < 16:
        return 'Слишком короткий номер'
    elif len(numb_card) > 16:
        return 'Слишком длинный номер'
    else:
        numb_card = list(numb_card)
        numb_card_new = []
        for i in numb_card[0:4]:
            numb_card_new.append(i)
        for star in numb_card[4:]:
            star = '*'
            numb_card_new.append(star)
        return ' '.join(numb_card_new)


print(card())
