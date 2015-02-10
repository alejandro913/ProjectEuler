# find largest palindrome made from two 3-digit numbers



def Palindrome(num): #finding if palindrome
    if num==num[::-1]:
        return True
    else:
        return False

x=100 #3 digit
y=100

biggest=0 #finding biggest product
while(x<=999): #while still 3 digits
    while(y<=999):
        mult=x*y #multiply to get product
        if(mult>biggest and Palindrome(str(mult))): #if the product is a palindrome
            biggest=mult #the biggest is now the biggest product
        y+=1
    y=100
    x+=1
print "Largest palindrome from two 3-digit numbers " + str(biggest)
    



