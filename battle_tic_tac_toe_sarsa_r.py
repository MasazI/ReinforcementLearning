#encoding: utf-8
'''
tic tac toe Sarsa学習
'''
from tic_tac_toe_sarsa_r_com import SarsaRCom
from tic_tac_toe_player import Player

from mark import Mark
from maru_mark import Maru
from batsu_mark import Batsu

from tic_tac_toe_game import Game

import dill

# モデルのロード
with open('tic_tac_toe_com_1_sarsa_r.pkl', 'rb') as f:
    com_1 = dill.load(f)

with open('tic_tac_toe_com_2_sarsa_r.pkl', 'rb') as f:
    com_2 = dill.load(f)

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

