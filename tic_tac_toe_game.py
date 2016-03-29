#encoding: utf-8
'''
tic tac toeゲームを対戦するクラス
'''
from mark import Mark
from maru_mark import Maru
from batsu_mark import Batsu
from empty_mark import Empty

from tic_tac_toe_state import State
from tic_tac_toe_player import Player

class Game:
    '''
    対戦クラス
    '''
    def __init__(self, maru_player, batsu_player):
        '''
        初期化
        arguments:
            Maru Player
            Batsu Player
        '''
        self.players = {1: maru_player, -1: batsu_player}

    def start(self, verbose=False):
        '''
        対戦の開始
        '''
        state = State()
        current_player_mark = 1
        result = None
        while(True):
            current_player = self.players[current_player_mark]
            if verbose:
                print("%s" % (state.to_array()))
            index = current_player.select_index(state)
            print("%s selected %i" % (self.players[current_player_mark].mark.to_string(), index))
            state = state.set(index, self.players[current_player_mark].mark)
            current_player.learn(0)

            if state.is_win(self.players[current_player_mark].mark):
                result = self.players[current_player_mark].mark
                # 勝者の報酬
                current_player.learn(1)
                # 敗者の報酬
                self.players[result.opponent().to_int()].learn(-1)
                if verbose:
                    print("%s" % (state.to_array()))
                    print("-"*5)
                    state.output()
                    print("-"*5)
                    print("%s win!!!" % (self.players[current_player_mark].mark.to_string()))
                break
            elif state.is_draw():
                result = Mark(Empty())
                for player in self.players:
                    player.learn(0)
                if verbose:
                    state.output()
                    print("draw.")
                break
            current_player_mark = self.players[current_player_mark].mark.opponent().to_int()

if __name__ == '__main__':
    player1 = Player(Mark(Maru()))
    player2 = Player(Mark(Batsu()))
    game = Game(player1, player2)
    game.start(verbose=True)
