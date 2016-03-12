# encoding: utf-8
'''
ブラックジャックのモンテカルロES法学習
'''

from mces import MCES
from blackjack_action_value import ActionValue
from blackjack_policy import Policy

import time


def do():
    '''
    ブラックジャックゲームの強化学習
    '''
    value = ActionValue()
    policy = Policy()
    mces = MCES(value, policy)

    epocs = 30
    stepsize = 100000

    for i in xrange(epocs+1):
        for j in xrange(stepsize+1):
            mces.simulate()
        print("#%d" % (i*stepsize))

        mces.action_value.output()
        mces.policy.output()

if __name__ == '__main__':
    start_time = time.time()
    do()    
    end_time = time.time()
    print("duration: %f[sec]" % (end_time - start_time))
