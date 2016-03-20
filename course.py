#encoding: utf-8
'''
レース用部品を使ったコースクラス
'''
from race import START
from race import COURSE1

import numpy as np

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
        return np.array(text.split(','), dtype=np.int)  

    def to_position(self, state):
        '''
        状態文字列から位置を取得
        arguments:
            状態文字列
        return:
            状態の位置を表す整数numpy配列[x, y]
        '''
        return self.to_position_speed(state)[0:2]
    
    def to_spped(self, state):
        '''
        状態文字列から速度を取得
        arguments:
            状態文字列
        return:
            状態の速度を表す整数numpy配列[x軸方向の速度、y軸方向の速度]
        '''
        return self.to_position_seed(state)[2:4]
    
    def to_course_info(self, state):
        '''
        状態文字列の位置からコースの状態情報を取得
        arguments:
            状態文字列
        return:
            コースの状態
        '''
        x, y = to_position(state)
        return self.source_info[y][x]

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



# test
if __name__ == '__main__':
        corse = Course(COURSE1)
                
