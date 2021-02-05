"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""


import random
from copy import deepcopy


class LotoCard:
    def __init__(self, name):
        self.__name = name
        self.list = self.__pattern_card__()
        self.nums = []

    def __pattern_card__(self):
        list = []
        for i in range(3):
            a = [1, 1, 1, 1, 1, 0, 0, 0, 0]
            random.shuffle(a)
            list.append(a)
        return list

    def card(self):
        for i in range(3):
            for j in range(9):
                if self.list[i][j]:
                    while True:
                        if j == 0:
                            n = random.choice(range(1, 10))
                        elif j == 8:
                            n = random.choice(range(80, 91))
                        else:
                            n = random.choice(range(j * 10, j * 10 + 10))
                        if n not in self.nums:
                            self.nums.append(n)
                            self.list[i][j] = n
                            break
                else:
                    self.list[i][j] = '  '
        return self.list


    def __str__(self):
        card_str = f'{self.__name}:\n{"-" * 26}\n'
        for line in self.card():
            card_str += f'{" ".join(str(x).ljust(2) for x in line)}\n'
        return card_str


class LotoGame(LotoCard):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def start(self):
        kegs = list(range(1, 91))
        while True:
            n = random.choice(kegs)
            kegs.remove(n)
            ans = input(f'{player1}\n{player2}\nБочонок {n} осталось {len(kegs)}\nХотите зачеркнуть? y/n: \n')
            if ans == 'y':
                if n not in player1:
                    print(f'{self.player1} проиграл!')
                else:
                    pass


player1 = LotoCard('Игрок')
player2 = LotoCard('Компьютер')
print(player1)
print((player1.nums))
#game = LotoGame(player1, player2)
# game.start()

