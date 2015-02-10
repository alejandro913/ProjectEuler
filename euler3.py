#largest prime factor of number 600851475143

x=600851475143 #number we want to find prime of
z=2 

while z**2<x: #making sure it is in fact a factor of the given number
    while x%z==0: #meaning it can be divided by and is a factor
        x=x/z # x is now the product of the original x divided by z
    z=z+1  # add one more to Z to find biggest number

print x
