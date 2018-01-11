import random
import Data,Block
'''初始化随机行人'''
def creatPeople():
    allBlock=[]#用于存放格子
    allPeople=[]#用于存放行人
    '''将所有格子全部存入列表'''
    for i in range(1,Data.ROOM_M):
        for j in range(1,Data.ROOM_N):
            b=Block.Block(1)
            b.x=i
            b.y=j
            if j>Data.ROOM_N/2:
                b.type=False
            else:
                b.type=True
            allBlock.append(b)
    '''随机排序'''
    random.shuffle(allBlock)
    '''取前N个'''
    '''可有效防止无限产生随机数'''
    allPeople=allBlock[:Data.PEOPLE_NUMBER]
    return allPeople

'''产生指定行人'''
def creatAppointPeo():
    allPeople=[]
    # b1=Block.Block(1)
    # b1.x=3
    # b1.y=5
    # b1.type=True
    # allPeople.append(b1)
    #
    # b2=Block.Block(1)
    # b2.x=4
    # b2.y=5
    # b2.type=False
    # allPeople.append(b2)

    b3 = Block.Block(1)
    b3.x = 10
    b3.y = 10
    b3.type = False
    allPeople.append(b3)

    b4 = Block.Block(1)
    b4.x = 16
    b4.y = 16
    b4.isNewDefine=1
    b4.force=30
    b4.type = False
    allPeople.append(b4)

    b5 = Block.Block(1)
    b5.x = 11
    b5.y = 11
    b5.isNewDefine = 0
    b5.type = False
    allPeople.append(b5)
    #
    # b6 = Block.Block(1)
    # b6.x = 12
    # b6.y = 12
    # b6.isNewDefine = 1
    # b6.type = False
    # allPeople.append(b6)
    #
    # b7 = Block.Block(1)
    # b7.x = 12
    # b7.y = 12
    # b7.isNewDefine = 1
    # b7.type = False
    # allPeople.append(b7)
    #
    # b8 = Block.Block(1)
    # b8.x = 12
    # b8.y = 12
    # b8.isNewDefine = 1
    # b8.type = False
    # allPeople.append(b8)
    #
    # b9 = Block.Block(1)
    # b9.x = 12
    # b9.y = 12
    # b9.isNewDefine = 1
    # b9.type = False
    # allPeople.append(b9)
    #
    # b11 = Block.Block(1)
    # b11.x = 12
    # b11.y = 12
    # b11.isNewDefine = 1
    # b11.type = False
    # allPeople.append(b11)

    return allPeople
'''产生墙壁'''
def creatWall():
    allWall=[]
    for i in range(5):
        D=[i,0]
        U=[i,2]
        allWall.append(D)
        allWall.append(U)
    return allWall
'''产生出口'''
def creatExit():
    allExit=[]
    for i in range(3):
        L=[0,i]
        R=[4,i]
        allExit.append(L)
        allExit.append(R)
    return allExit



