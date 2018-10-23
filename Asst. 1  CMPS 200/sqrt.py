import sys
a=float(sys.argv[1])
x=a
while abs(x**2-a) > 10**-7:
    x=(x+a/x)/2
print(x)    

