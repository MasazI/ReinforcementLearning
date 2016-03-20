#encoding: utf-8
'''
カーレース方策クラス
'''
from course import Course
import random

from race import COURSE1

from collections import defaultdict

class PolicyDict(dict):
    '''
    状態文字列によって初期値の範囲が異なる方策辞書
    '''
    def __init__(self, course):
        self.course = course

    def __missing__(self, key):
        value = self.course.get_valid_actions(key)
        self[key] = random.choice(value)
        return self[key]

class RacePolicy:
    '''
    方策クラス
    '''
    def __init__(self, course):
        self.course = course
        self.policy = PolicyDict(course)


    def get_action(self, state):
        '''
        方策に従った行動の取得
        arguments:
            状態文字列
        return:
            行動文字列
        '''
        return self.policy[state]

    def set_action(self, state, action):
        '''
        方策(状態と行動の決定論的方策)の設定(ソフトな方策にする場合には呼び出し側でコントロール)
        arguments:
            状態文字列
            行動
        '''
        self.policy[state] = action


if __name__ == '__main__':
    race_policy = RacePolicy(Course(COURSE1))
    print("default: state[1,3,1,-1], %s" % (race_policy.get_action("1,3,1,-1")))
    print("get policy: state[1,3,1,-1], %s" % (race_policy.get_action("1,3,1,-1")))
    race_policy.set_action("1,3,1,-1", "3,3")
    print("set and get policy: state[1,3,1,-1], %s" % (race_policy.get_action("1,3,1,-1")))
   
    

 
