# ANDゲートの作成
def AND(a,b):
    w1    = 0.5
    w2    = 0.5
    theta = 1.0
    
    #閾値を超えるかの判断に使う式
    D = w1*a + w2*b
    
    if D>=theta:
        return 1
    else:
        return 0

# NANDゲートの作成
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
        
# ORゲートの作成
def OR(a,b):
    w1    = 0.5
    w2    = 0.5
    theta = 0.5
    
    #閾値を超えるかの判断に使う式
    D = w1*a + w2*b
    
    if D>=theta:
        return 1
    else:
        return 0

# XORゲート
def XOR(a,b):
    s1 = NAND(a,b)
    s2 = OR(a,b)
    y = AND(s1,s2)
    
    return y

# 実践
li = [XOR(1,1),XOR(1,0),XOR(0,1),XOR(0,0)]

for i in li:
    print(i)
    