natural, sum = 0, 0 
while(natural<1000):
    if(natural%5==0 or natural%3==0):
        sum = sum + natural
    natural += 1

print sum
