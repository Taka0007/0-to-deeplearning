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
        
# 実践
li = [AND(1,1),AND(1,0),AND(0,1),AND(0,0)]

for i in li:
    print(i)
