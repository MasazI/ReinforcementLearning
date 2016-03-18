# encoding: utf-8
'''
ブラックジャックのモンテカルロES法学習
'''

from mc_on_policy import MCONP
from blackjack_action_value import ActionValue
from blackjack_on_policy import Policy

import time


def do():
    '''
    ブラックジャックゲームの強化学習
    '''
    value = ActionValue()
    policy = Policy()
    mconp = MCONP(value, policy, 0.1)

    epocs = 30
    stepsize = 100000

    for i in xrange(epocs+1):
        for j in xrange(stepsize+1):
            mconp.simulate()
        print("#%d" % (i*stepsize))

        mconp.action_value.output()
        mconp.policy.output()

if __name__ == '__main__':
    start_time = time.time()
    do()    
    end_time = time.time()
    print("duration: %f[sec]" % (end_time - start_time))
