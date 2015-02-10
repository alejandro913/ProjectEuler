
#assign variables
x=0
y=1
solution=0  #the final solution that we will print

while y <=4000000:  #since we are stopping at 4mil
    if y%2==0: #only counting the evens
        solution+=y # creating sum of even values
    x,y= y, x+y #this is where fib happens, add the previous two values together to make the new one

print (solution)
    
