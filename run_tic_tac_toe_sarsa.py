#encoding: utf-8
'''
tic tac toe Sarsa学習
'''
from tic_tac_toe_value import Value
from tic_tac_toe_sarsa_com import SarsaCom
from tic_tac_toe_player import Player

from mark import Mark
from maru_mark import Maru
from batsu_mark import Batsu
from empty_mark import Empty

from tic_tac_toe_state import State

from tic_tac_toe_game import Game

# 共通行動価値テーブル
value = Value()

print("Sarsa method:")
print("Training com1 and com2.")

com_1 = SarsaCom(Mark(Maru()), value)
com_2 = SarsaCom(Mark(Batsu()), value)

print("Input the number of iterations:")

iterations = 10000
while(True):
    input_line = raw_input()
    if input_line.isdigit():
        iterations = int(input_line)
        break
    else:
        print("Input number:")

for i in xrange(iterations):
    game = Game(com_1, com_2)
    game.start()
    if i % 1000 == 0:
        print("training iterations: No.%d" % (i))


com_1.training = False
com_2.training = False

while(True):
    print("Select a type of fight [1, 2, 3, q]")
    print("1: human vs com2")
    print("2: com1 vs human")
    print("3: com1 vs com2")
    print("q: quit")    

    type_of_fight = 1
    input_line = raw_input()
    if input_line.isdigit():
        type_of_fight = int(input_line)
    else:
        if input_line == 'q':
            break
        continue

    if type_of_fight == 1:
        game = Game(Player(Mark(Maru())), com_2)
    elif type_of_fight == 2:
        game = Game(com_1, Player(Mark(Batsu())))
    elif type_of_fight == 3:
        game = Game(com_1, com_2)
    game.start(True)

