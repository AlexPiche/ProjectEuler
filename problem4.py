factor1 = 999
factor2 = factor1
highest = 0

while(factor1>99):
    while(factor2>99):
        product = factor1*factor2
        product = str(product)

        invProduct = product[::-1]

        if(product==invProduct and int(product) > int(highest)):
            highest = product

        factor2 -= 1
    factor1 -= 1
    factor2 = factor1
print highest


