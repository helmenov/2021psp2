#%% newton2.py 
x = 3 
for n in range(10000): 
    epsilon = (x**2-3) / (2*x)
    x_next = x - epsilon 
    print(n+1,':',x_next)
    if (x_next - x) ** 2 < 0.001: 
         break 
    x = x_next 