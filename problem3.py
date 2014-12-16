import pdb

number = 600851475143.0
prime = int(number**(0.5))


while(prime>2):
    prime -= 1
    if(number%prime==0):
        i=2
        while(i<=prime):
            if(i==prime):
                print prime
                break
            if(prime%i!=0):
                i += 1
            else:
                i = prime + 1




