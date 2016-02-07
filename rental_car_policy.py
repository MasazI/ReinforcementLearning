#encoding: utf-8
'''
方策(Policy)クラス
'''

import rental_car_util as util
import numpy as np

class Policy:
    '''
    方策(Policy)
    '''
    def __init__(self):
        self.rcu = util.RentalCarUtil()

        # 状態ごとのPolicy(整数)
        self.policy = np.zeros([self.rcu.MAX_NUM_RENTAL_CAR, self.rcu.MAX_NUM_RENTAL_CAR], dtype=np.int)
        print("policy shape: ")
        print(self.policy.shape)

        self.print_boundary = "====" + ("====" * self.rcu.MAX_NUM_RENTAL_CAR)
        self.print_bar = "----" + ("----" * self.rcu.MAX_NUM_RENTAL_CAR)
        self.print_header = "   |"
        for i in xrange(self.rcu.MAX_NUM_RENTAL_CAR):
            self.print_header += " %02d " % (i+1)

    def get_policy(self, x, y):
        '''
        状態(x, y)に対するPolicyを取得
        arguments:
            x: 第1営業所の状態
            y: 第2営業所の状態
        return:
            状態(x, y)に対するPolicy
        '''
        return self.policy[x][y]
    
    def set_policy(self, x, y, move):
        '''
        状態(x,y)のPolicy(整数)を設定
        arguments:
            x: 第1営業所の状態
            y: 第2営業所の状態
            move: Policy(移動量)
        ''' 
        self.policy[x][y] = move

    def output(self):
        '''
        Policyの出力
        '''
        print self.print_boundary
        print "P(s, a)"
        print self.print_bar
        print self.print_header
        print self.print_bar
        for j in xrange(self.rcu.MAX_NUM_RENTAL_CAR):
            print_format = "%02d |" % (j+1)
            for i in xrange(self.rcu.MAX_NUM_RENTAL_CAR):
                print_format += " %02d " % self.policy[i][j]
            print print_format


def test():
    policy = Policy()
    print policy.get_policy(2,3)
    policy.set_policy(1,2,-3)
    policy.set_policy(3,4,4)
    policy.output()

if __name__ == '__main__':
    test()
