#%% newton1.py 
x = 3
for n in range(10): 
    epsilon = (x**2-3)/(2*x)
    x = x - epsilon 
    print(n+1,':',x)
    