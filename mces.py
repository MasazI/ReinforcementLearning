# encoding: utf-8
'''
モンテカルロES法クラス
'''

import blackjack
import blackjack_action_value
import blackjack_policy

class MCES:
    def __init__(self, action_value, policy):
        '''
        初期化
        arguments:
            行動価値
            方針(Policy)
        '''
        self.action_value = action_value
        self.policy = policy


        
