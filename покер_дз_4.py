class Card:
    def __init__(self, mast, dignity):
        self.mast = mast
        self.dignity = dignity


class Hand:
    def __init__(self, cards=[]):
        self.cards = cards

def cards_sort(cards):
    dictionary_name_key = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Валет': 11,
                           'Дама': 12, 'Король': 13, 'Туз': 14}
    for i in range(len(cards)-1):
        for j in range(i+1, len(cards)):
            if dictionary_name_key[cards[i].dignity] > dictionary_name_key[cards[j].dignity]:
                cards[i], cards[j] = cards[j], cards[i]

    return cards

def flash_royal_check(cards):
    dictionary_name_key = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Валет': 11,
                           'Дама': 12, 'Король': 13, 'Туз': 14}
    for i in range(len(cards)-1):
        if cards[i].mast != cards[i+1].mast:
            return False
    for i in range(len(cards)-1):
        if dictionary_name_key[cards[i].dignity] != dictionary_name_key[cards[i+1].dignity]-1:
            return "Флеш"
    if cards[len(cards)-1].dignity == "Туз":
           return "Флеш рояль"
    return "Стрит флеш"


def care_check(cards):
    if cards[0].dignity != cards[1].dignity:
        for i in range(1, len(cards)):
            if cards[i].dignity != cards[i+1].dignity:
                return False
    else:
        for i in range(1, len(cards)-2):
            if cards[i].dignity != cards[i+1].dignity:
                return False
    return 'Каре'

def full_chaos_check(cards):
    if cards[0].dignity == cards[1].dignity:
        if cards[1].dignity == cards[2].dignity and cards[3].dignity == cards[4].dignity or cards[2].dignity == cards[3].dignity and cards[3].dignity == cards[4].dignity:
            return 'Фулл хаус'
    return False

def straight_check(cards):
    for i in range(len(cards) - 1):
        if dictionary_name_key[cards[i].dignity] != dictionary_name_key[cards[i + 1].dignity] - 1:
            return False
    return 'Стрит'

def set_three_check(cards):
    if (cards[0].dignity == cards[1].dignity and cards[1].dignity == cards[2].dignity) or (
            cards[1].dignity == cards[2].dignity and cards[2].dignity == cards[3].dignity) or (
            cards[2].dignity == cards[3].dignity and cards[3].dignity == cards[4].dignity):
        return 'Сет'
    return False

def two_double_check(cards):
    if cards[0].dignity == cards[1].dignity:
        if cards[2].dignity == cards[3].dignity or cards[3].dignity == cards[4].dignity:
            return 'Две пары'
    elif cards[1].dignity == cards[2].dignity and cards[3].dignity == cards[4].dignity:
        return 'Две пары'
    return False

def double_check(cards):
    for i in range(len(cards)-1):
        if cards[i].dignity == cards[i+1].dignity:
            return 'Пара'
    return False

def combination_check(cards):
    cards = cards_sort(cards)
    if flash_royal_check(cards) != False:
        return flash_royal_check(cards)
    if care_check(cards) != False:
        return care_check(cards)
    if full_chaos_check(cards) != False:
        return full_chaos_check(cards)
    if straight_check(cards) != False:
        return straight_check(cards)
    if set_three_check(cards) != False:
        return set_three_check(cards)
    if two_double_check(cards) != False:
        return two_double_check(cards)
    if double_check(cards) != False:
        return double_check(cards)
    return 'Старшая карта'

def cards_print(cards):
    for i in cards:
        print(i.dignity, i.mast)



dictionary_name_key = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Валет': 11,
                       'Дама': 12, 'Король': 13, 'Туз': 14}


flash_royal = Hand(
    [Card('Пики', 'Туз'), Card('Пики', 'Король'), Card('Пики', 'Дама'), Card('Пики', 'Валет'), Card('Пики', '10')])

straight_flash = Hand(
    [Card('Черви', '7'), Card('Черви', '8'), Card('Черви', '9'), Card('Черви', '10'), Card('Черви', 'Валет')])

care = Hand([Card('Буби', '5'), Card('Черви', '5'), Card('Пики', '5'), Card('Крести', '5'), Card('Пики', 'Валет')])

full_chaos = Hand(
    [Card('Пики', '8'), Card('Крести', '8'), Card('Буби', 'Туз'), Card('Черви', 'Туз'), Card('Крести', 'Туз')])

flash = Hand(
    [Card('Крести', 'Туз'), Card('Крести', 'Валет'), Card('Крести', '7'), Card('Крести', '4'), Card('Крести', '2')])

straight = Hand(
    [Card('Черви', '7'), Card('Крести', '8'), Card('Буби', '9'), Card('Буби', '10'), Card('Крести', 'Валет')])

set_three = Hand(
    [Card('Буби', '8'), Card('Пики', '8'), Card('Крести', '8'), Card('Буби', '6'), Card('Пики', 'Король')])

two_double = Hand(
    [Card('Буби', 'Туз'), Card('Черви', 'Туз'), Card('Пики', '5'), Card('Крести', '5'), Card('Пики', '3')])

double = Hand(
    [Card('Буби', 'Туз'), Card('Черви', 'Туз'), Card('Буби', '6'), Card('Пики', '7'), Card('Пики', 'Валет')])

older_card = Hand(
    [Card('Пики', 'Дама'), Card('Крести', 'Валет'), Card('Буби', '3'), Card('Черви', '5'), Card('Буби', '8')])

combination = [flash_royal, straight_flash, care, full_chaos, flash, straight, set_three, two_double, double, older_card]
for i in combination:
    print('Текущие карты:')
    cards_print(i.cards)
    print(combination_check(i.cards))
    print()
