#encoding:utf-8
'''
価値反復(Value iteration)
'''

import rental_car_util as util
import numpy as np

import rental_car_policy
import rental_car_status_value

class ValueIteration:
    '''
    価値反復クラス
    '''
    def __init__(self, value, policy, verbose=False):
        self.value = value
        self.policy = policy
        self.verbose = verbose
        self.rcu = util.RentalCarUtil()
        self.move_range = tuple(range(-self.rcu.MAX_NUM_MOVE, self.rcu.MAX_NUM_MOVE+1))

    def do(self):
        i = 0
        while(True):
            delta = 0.0

            for x in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
                for y in xrange(self.rcu.MAX_NUM_RENTAL_CAR+1):
                    # 現在の値をテンポラリーに保存
                    old_value = self.value.get(x, y)

                    new_policy, new_value = self.value.get_most_valuable_move(x, y, self.move_range)

                    # 毎回状態価値と方策に反映
                    self.value.set(x, y, new_value)
                    self.policy.set_policy(x, y, new_policy)

                    delta = max([delta, abs(new_value - old_value)])

            if self.verbose:
                print("V(s)_%d" % (i))
                self.value.output()
                print("P(s, a)_%d" % (i))
                self.policy.output()

            if delta < self.rcu.delta_max:
                break
            else:
                i += 1

def execute():
    value = rental_car_status_value.StatusValue()
    policy = rental_car_policy.Policy()

    value_iteration = ValueIteration(value, policy, True)
    
    value_iteration.do()

    print("optimized status value function: 最適状態価値関数")
    value_iteration.value.output()

    print("optimized policy: 最適方策")
    value_iteration.policy.output()


if __name__ == '__main__':
    execute()    
