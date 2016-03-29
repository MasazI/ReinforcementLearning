# encoding: utf-8
'''
tic tac toe 手動ゲーム対戦
'''
from mark import Mark
from maru_mark import Maru
from batsu_mark import Batsu

from tic_tac_toe_player import Player
from tic_tac_toe_game import Game

if __name__ == '__main__':
    print("Start Game...")
    player1 = Player(Mark(Maru()))
    player2 = Player(Mark(Batsu()))
    game = Game(player1, player2)
    game.start(verbose=True)
