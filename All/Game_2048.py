# /2048
# 模块： 1、一次按钮后生成一个随机数
#         2、能显示分数
#        3、刷新函数 ❌
import random

def refresh():  # function for refresh numbers
    for i in range(4):
        print()
        for j in range(4):
            # if b[i][j] == 0:
            #     print('  ', end=' ')
            # else:
                print(b[i][j], end=' ')
    print()

def random_num():  # 在空位产生随机数
    def part_1(hang, lie):
        num = [2,2,2,4,4, 8]
        b[hang][lie] = num[random.randint(0, 5)]
    while 1:
        hang= random.randint(0,3)
        lie = random.randint(0,3)
        if b[hang][lie] == 0:
            part_1(hang, lie)
            break

def toward(key):
    def carry_heng(con):
        if con == 'l':
            st, end, step = (1, 4, 1)
            lie, heng = (0, -1)
        if con == 'r':
            st, end, step = (-2, -5, -1)
            lie, heng = (0, 1)
        for k in range(3):
            for i in range(4):
                for j in range(st, end, step):
                    if b[i + lie][j + heng] == 0 and b[i][j] != 0:
                        b[i + lie][j + heng] = b[i][j]
                        b[i][j] = 0
                    elif b[i + lie][j + heng] == b[i][j]:
                        b[i + lie][j + heng] *= 2
                        b[i][j] = 0
        random_num()
        refresh()
    def carry_lie(con):  # 根据给出的方向移动数字方块
        if con == 'u':
            st, end, step = (1, 4, 1)
            lie, heng = (-1, 0)
        if con == 'd':
            st, end, step = (-2, -5, -1)
            lie, heng = (1, 0)
        for k in range(3):
            for j in range(4):
                for i in range(st, end, step):
                    if b[i + lie][j + heng] == 0 and b[i][j] != 0:
                        b[i + lie][j + heng] = b[i][j]
                        b[i][j] = 0
                    elif b[i + lie][j + heng] == b[i][j]:
                        b[i + lie][j + heng] *= 2
                        b[i][j] = 0
        random_num()
        refresh()

    if key == 'w':
        carry_lie('u')
    if key == 's':
        carry_lie('d')
    if key == 'a':
        #add()
        carry_heng('l')
    if key == 'd':
        carry_heng('r')

a = [0,0,0,0]
b = [a, a.copy(), a.copy(),a.copy()]
while 1:
    toward(input())