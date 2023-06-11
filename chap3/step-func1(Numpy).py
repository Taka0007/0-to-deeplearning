# Numpy配列にも対応
import numpy as np

def step_func(X):
    y = X>0
    return y.astype(int)

arr = np.array([-1.0, -11.11, 2.0, 6.0])
print(step_func(arr))

# 簡単に概要をまとめると、
# 配列をbool変換して、それを整数型に直す(1,0)にしているだけ
# 与えられた数字が0より大きかったら1、そうでないなら0を返すようにしているだけ