def sayed(b):
    def inner(a):
        sum=0
        for i in range(a+1):
            if i%2!=0 : 
                sum=sum+i
        print("sum of odd of  ",sum)
        return b(a)
    return inner
@sayed
    
def b(a):
    print("")
b(101)   