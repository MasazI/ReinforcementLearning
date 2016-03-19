#encoding: utf-8
'''
レース用部品を使ったコースクラス
'''
from race import START
from race import COURSE1

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
        位置と速度
        arguments:
            x軸の座標
            y軸の座標
            x軸に対する速度
            y軸に対する速度
        '''
        return ",".join([str(x), str(y), str(vx), str(vy)])
        

# test
if __name__ == '__main__':
    corse = Course(COURSE1)
                
