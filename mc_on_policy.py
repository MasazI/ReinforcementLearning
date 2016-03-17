# encoding: utf-8
'''
方策ONモンテカルロ法クラス
'''

from blackjack import Blackjack
from blackjack_action_value import ActionValue
from blackjack_policy import Policy

from collections import deque
import random

class MCONP:
    '''
    方策ONモンテカルロ
    '''
    def __init__(self, action_value, policy, epsilon):
        '''
        初期化
        arguments:
            行動価値
            方針(Policy)
            イプシロン
        '''
        self.action_value = action_value
        self.policy = policy
        self.epsilon = epsilon

    def simulate(self, verbose=False, train=True):
        '''
        シュミレーション(ゲームを1回実行して価値観数と方策を更新する)
        '''
        game = Blackjack()
        if verbose:
            print("[blackjack simulate]:")
            game.output()
            print game.dealer_face_value()

        player_total_queue = deque()
        player_has_ace_queue = deque()
        player_hit_queue = deque()
        dealer_face_value = game.dealer_face_value()

        while(True):
            player_total = game.player_total
            player_has_ace = game.player_has_ace()

            # モンテカルロESのES
            # 最初の行動はExploring Starts(ランダムに選択)
            #if not player_hit_queue:
            #    player_hit = random.choice([True, False])
            #else:
                # 方策によって行動を選択
            #    player_hit = self.policy.hit(player_total, player_has_ace, dealer_face_value)

            # 方策ONなので方策によって行動を選択
            player_hit = self.policy.hit(player_total, player_has_ace, dealer_face_value)

            if train:
                # ε-greedy
                select = random.random()
                for i, action in enumerate((True, False)):
                    if select < ((self.epsilon / 2) * (i+1))
                        player_hit = action
                        break


            # キューに追加
            player_total_queue.append(player_total)
            player_has_ace_queue.append(player_has_ace)
            player_hit_queue.append(player_hit)

            if player_hit:
                game.player_hit()
                if verbose:
                    game.output()
                if game.finish:
                    break
            else:
                game.player_stand()
                if verbose:
                    game.output()
                break

        # 勝敗を確認(報酬)
        result = game.judgement_result()
        if verbose:
            print("result: %s" % (result))

        # 今回の行動、状態、報酬によって行動価値を更新
        for player_total, player_has_ace, player_hit in zip(player_total_queue, player_has_ace_queue, player_hit_queue):
            self.action_value.update(player_total, player_has_ace, dealer_face_value, player_hit, result)

        # 方策を更新（1ゲームごとに更新する）
        for player_total, player_has_ace in zip(player_total_queue, player_has_ace_queue):
            # 今回の状態でヒットした場合の価値
            hit_value = self.action_value.get(player_total, player_has_ace, dealer_face_value, True)
            # 今回の状態でスタンドした場合の価値
            stand_value = self.action_value.get(player_total, player_has_ace, dealer_face_value, False)

            if hit_value > stand_value:
                # ヒットの価値が高ければ方策をヒットに更新
                self.policy.set(player_total, player_has_ace, dealer_face_value, True)
            elif hit_value < stand_value:
                # ヒットの価値が低ければ方策をスタンドに更新
                self.policy.set(player_total, player_has_ace, dealer_face_value, False)

def test():
    action_value = ActionValue()
    policy = Policy()
    mces = MCES(action_value, policy)
    mces.simulate(verbose=True)
    mces.action_value.output()
    mces.policy.output()


if __name__ == '__main__':
    test()
