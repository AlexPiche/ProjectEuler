import math

smallest = 20

stop = math.factorial(20)

while(smallest<stop):
    divider = 3
    while(divider <= 20):
        if(smallest%divider!=0):
            divider = 21
            smallest += 2
        else:
            divider += 1
            if(divider==21):
                print smallest
                smallest = stop + 1



