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
        
# 実践
li = [OR(1,1),OR(1,0),OR(0,1),OR(0,0)]

for i in li:
    print(i)
