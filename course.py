#encoding: utf-8
'''
レース用部品を使ったコースクラス
'''
from race import START
from race import COURSE1
from race import MAX_SPEED
from race import OUT
from race import IN
from race import GOAL

import numpy as np
import math

class Course:
    def __init__(self, course):
        '''
        コースの初期化
        '''
        self.course_info = []
        self.starts = []

        lines = course.splitlines()
        for j, line in enumerate(lines):
            line_info = []
            for i, char in enumerate(line):
                line_info.append(char)
                if char == START:
                    self.starts.append(self.to_state(i, j, 0, 0))      

            self.course_info.append(line_info)

    def get_valid_actions(self, state):
        '''
        選択可能な行動の集合を取得
        状態は現在からx軸, y軸方向にそれぞれ-1~+1まで変更可能
        arguments:
            状態文字列
        return:
            選択可能な行動文字列の配列
        '''
        vx, vy = self.to_speed(state)
        
        valid_actions = []
        for ax in xrange(-1,2):
            for ay in xrange(-1,2):
                new_vx = vx + ax
                new_vy = vy + ay
                if (math.fabs(new_vx) <= MAX_SPEED) and (math.fabs(new_vy) <= MAX_SPEED) and (math.fabs(new_vx) + math.fabs(new_vy) > 0):
                    valid_actions.append(self.to_action(ax, ay))
        return valid_actions

    def step(self, state, action):
        '''
        ある状態から行動して次の状態と報酬を取得する
        arguments:
            state: 状態文字列
            action: 行動文字列
        return:
            next_state: next state string
            reward
        '''
        x, y, vx, vy = self.to_position_speed(state)
        ax, ay = self.to_ax_ay(action)

        vx += ax
        vy += ay

        # 移動後の位置
        new_x = x + vx
        new_y = y + vy

        if self.get_course_info(new_x, new_y) == OUT:
            next_state = self.to_state(x, y, vx, vy)
            reward = -5
        else:
            next_state = self.to_state(new_x, new_y, vx, vy)
            reward = -1
        return next_state, reward


    def to_state(self, x, y, vx, vy):
        '''
        状態文字列の生成(位置と速度)
        arguments:
            x軸の座標
            y軸の座標
            x軸に対する速度
            y軸に対する速度
        return:
            状態文字列
        '''
        return ",".join([str(x), str(y), str(vx), str(vy)])

    def to_position_speed(self, state):
        '''
        状態文字列から位置を速度情報を取得
        arguments:
            状態文字列
        return:
            状態の位置と速度を表す整数値numpy配列[x, y , vx, vy]
        '''
        return np.array(state.split(','), dtype=np.int)  

    def to_position(self, state):
        '''
        状態文字列から位置を取得
        arguments:
            状態文字列
        return:
            状態の位置を表す整数numpy配列[x, y]
        '''
        return self.to_position_speed(state)[0:2]
    
    def to_speed(self, state):
        '''
        状態文字列から速度を取得
        arguments:
            状態文字列
        return:
            状態の速度を表す整数numpy配列[x軸方向の速度、y軸方向の速度]
        '''
        return self.to_position_speed(state)[2:4]
    
    def to_course_info(self, state):
        '''
        状態文字列の位置からコースの状態情報を取得
        arguments:
            状態文字列
        return:
            コースの状態
        '''
        x, y = self.to_position(state)
        return self.get_course_info(x, y)

    def get_course_info(self, x, y):
        '''
        位置情報からコースの情報を取得
        arguments:
            y: y軸方向の位置
            x: x軸方向の位置
        return:
            指定した位置におけるコースの状態
        '''
        try:
            course_state = self.course_info[y][x]
        except Exception as e:
            print("y: %d, x: %d" % (y, x))
            print(e)
        return course_state

    def to_action(self, ax, ay):
        '''
        行動文字列の生成
        arguments:
            ax: x軸方向の行動
            ay: y軸方向の行動
        return:
            行動文字列
        '''
        return ",".join([str(ax), str(ay)])

    def to_ax_ay(self, action):
        '''
        行動文字列から行動を取得
        arguments:
            行動文字列
        return:
            行動を表す整数numpy配列[x軸方向の行動, y軸方向の行動]
        '''
        return np.array(action.split(','), dtype=np.int)

    ## 現在の状態文字列の位置について、状態を取得
    def is_in(self, state):
        '''
        状態がINかどうか
        arguments:
            状態文字列
        return:
            INの場合はTrue, INでない場合はFalse
        '''
        return self.to_course_info(state) == IN

    def is_out(self, state):
        '''
        状態がOUTかどうか
        arguments:
            状態文字列
        return:
            OUTの場合はTrue, OUTでない場合はFalse
        '''
        return self.to_course_info(state) == OUT

    def is_start(self, state):
        '''
        状態がSTARTかどうか
        arguments:
            状態文字列
        return:
            STARTの場合はTrue, STARTでない場合はFalse
        '''
        return self.to_course_info(state) == START

    def is_goal(self, state):
        '''
        状態がGOALかどうか
        arguments:
            状態文字列
        return:
            GOALの場合はTrue, GOALでない場合はFalse
        '''
        return self.to_course_info(state) == GOAL

# test
if __name__ == '__main__':
        course = Course(COURSE1)
        print("course#to_state %s" % (course.to_state(1, 2, 3, 4)))
        print("course#to_position_speed %s" % (course.to_position_speed("1,2,3,4")))
        print("course#to_position %s" % (course.to_position("1,2,3,4")))
        print("course#to_speed %s" % (course.to_speed("1,2,3,4")))
        print("course#to_course_info %s" % (course.to_course_info("1,2,3,4")))
        print("course#get_course_info %s" % (course.get_course_info(1, 2)))
        print("course#to_action %s" % (course.to_action(-3, 4)))
        print("course#to_ax_ay %s" % (course.to_ax_ay("-3,4")))
        print("course#get_valid_actions %s" % (course.get_valid_actions("5,6,1,-1")))
        print("course#step new_state:%s reward:%s" % (course.step("4,5,-1,1", "0,2")))
