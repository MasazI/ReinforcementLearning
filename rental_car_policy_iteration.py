#encoding: utf-8
'''
方策反復(Policy iteration)
'''

import rental_car_util as util
import numpy as np

import rental_car_policy
import rental_car_status_value

class PolicyIteration:
    '''
    方策反復クラス
    '''
    def __init__(self, value, policy, verbose=False):
        self.value = value
        self.policy = policy
        self.verbose = verbose

        # 定数
        self.rcu = util.RentalCarUtil()

        # 行動の範囲
        self.move_range = tuple(range(-self.rcu.MAX_NUM_MOVE, self.rcu.MAX_NUM_MOVE+1))



    def do(self):
        '''
        反復の実行
        '''
        i = 0
        while(True):
            # 方策の評価
            self.evaluate_policy()

            if self.verbose:
                print("V(s)_%d" % (i))
                self.value.output()

            # 方策の改善
            updated = self.improve_policy()
            if self.verbose:
                print("P(s,a)_%d" % (i))
                self.policy.output()

            if updated:
                i += 1
            else:
                break
  
    def evaluate_policy(self):
        while(True):
            delta = 0.0

            for x in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
                for y in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
                    # 現在の状態評価をテンポラリーに保存
                    old_value = self.value.get(x, y)

                    # 状態(x,y)に対するPolicyに従った行動の価値
                    new_value = self.value.value_of_move(x, y, self.policy.get_policy(x, y))

                    # 改善幅deltaの更新
                    delta = max(delta, abs(new_value - old_value))

                    # 状態価値に新しい値を設定
                    self.value.set(x, y, new_value)

            if delta < self.rcu.delta_max:
                break
        if self.verbose:
            print("evaluta_policy: ")
            self.value.output() 


    def improve_policy(self):
        '''
        状態価値V(s)を利用した方策(Policy)の改善
        return:
            updated:
                True: 改善した
                False: 改善していない
        '''
        updated = False

        for x in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
            for y in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
                # 現在のポリシーをテンポラリーに保存
                old_policy = self.policy.get_policy(x, y)

                # 状態(x,y)に対するもっとも価値の高い行動を取得
                new_policy, max_value = self.value.get_most_valuable_move(x, y, self.move_range)

                if old_policy != new_policy:
                    print "updated!"
                    updated = True
                    self.policy.set_policy(x, y, new_policy)
                else:
                    print "not updated."
        return updated



def test():
    policy_iteration = PolicyIteration(1,2)
    #policy_iteration.do()
    print("actions: ")
    print tuple(range(-policy_iteration.rcu.MAX_NUM_RENTAL_CAR, policy_iteration.rcu.MAX_NUM_RENTAL_CAR+1))


def execute():
    value = rental_car_status_value.StatusValue()
    policy = rental_car_policy.Policy()

    policy_iteration = PolicyIteration(value, policy, True)
    policy_iteration.do()
   
    print("optimized status value function: 最適状態価値関数") 
    policy_iteration.value.output()

    print("optimized policy: 最適方策")
    policy_iteration.policy.output()

if __name__ == '__main__':
    #test()
    execute()
