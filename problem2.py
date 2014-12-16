import numpy as np

Fibonacci = {}
Fibonacci[0] = 0
Fibonacci[1] = 1
last = 1

sum =0

while(Fibonacci[last]<4*10**6):
    last += 1
    Fibonacci[last] = Fibonacci[last-1] + Fibonacci[last-2]
    if(Fibonacci[last]%2 == 0):
        sum = sum + Fibonacci[last]

print sum
