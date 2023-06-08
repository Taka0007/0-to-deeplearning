def step_func(N):
    if N>0:
        return 1
    else:
        return 0
        
li = [2,3,-1,0]
for num in li:
    print(step_func(num))