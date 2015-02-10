# smallest positive number that is evenly divisible by all numbers from 1-20


'''
def Solution(numbs):
    for num in range(100,999999999):
        for x in range(11,21):
            if num%x==0:
                return num
    return None

#kept giving me 20 or 100 as response so I found someone who did it a but different

'''



chk_lst=[11,12,13,14,15,16,17,18,19,20]


def Solution(numbs):
    for num in xrange(numbs,999999999,numbs):
        if all(num%x==0 for x in chk_lst):
            return num
    return None



     
if __name__== "__main__":
    solu=Solution(20)
    if solu is None:
        print "No answer"
    else:
        print "Answer: "+ str(solu)
            





