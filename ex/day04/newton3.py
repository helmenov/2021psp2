#%% newton3.py 
 
x_list = [3, -3]
n_loop = 10000 
error_limit = 0.001 

for x in x_list: 
    for n in range(n_loop): 
        epsilon = (x**2-3)/(2*x)
        x_next = x - epsilon 
        if (x_next - x)**2 < error_limit: 
              break 
        x = x_next
    print(x) 
    