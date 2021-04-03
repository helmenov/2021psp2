str1 = input('Please input number->')
print(str1,type(str1))
integer=int(str1)
oddeven=integer%2
print(oddeven)
if oddeven == 0 :
    print("even")
elif oddeven == 1:
    print("odd")
else:
    print("wrong number")
