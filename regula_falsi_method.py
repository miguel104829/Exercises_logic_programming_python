#create program of regula falsi method
import math
#function to be solved
def f(x):
    return -1/10*x**2 + 3
#function to find the root
def regulaFalsi(a,b):
    if f(a)*f(b) >= 0:
        print("You have not assumed right a and b\n")
        return -1
    c = a # Initialize result
    for i in range(100):
        # Find the point that touches x axis
        c = (a*f(b) - b*f(a))/ (f(b) - f(a))
        # Check if the above found point is root
        if f(c) == 0:
            break
        # Decide the side to repeat the steps
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ","%.4f"%c)
# Driver code to test above function
# Initial values assumed
a =1
b =7
regulaFalsi(a, b)