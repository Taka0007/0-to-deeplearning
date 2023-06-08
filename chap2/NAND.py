# NANDゲートの作成
# ANDの大小を逆転させるだけ
def NAND(a,b):
    w1    = 0.5
    w2    = 0.5
    theta = 1.0
    
    #閾値を超えるかの判断に使う式
    D = w1*a + w2*b
    
    if D<theta:
        return 1
    else:
        return 0
        
# 実践
li = [NAND(1,1),NAND(1,0),NAND(0,1),NAND(0,0)]

for i in li:
    print(i)
