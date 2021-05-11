#%%
from mypack import mymodule04 as my

def FuncOne(x): 
     return x ** 2 - 3 

def FuncTwo(x): 
     return x**2- 10

def FuncThree(x):
    return x**2+2*x-3

xList = [-3,3]# 初期値のリスト
nLoop = 100 # 繰り返し回数
errorLimit = 0.0001 #　解の収束判定条件

for x_0 in xList: 
    x = my.NewtonSolver(TargetFunc=FuncThree, x=x_0, n_loop=nLoop, error_limit=errorLimit)
    print(x) 