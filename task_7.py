def sayed(b):
    def inner(a):
        sum=0
        for i in range(a+1):
            if i%4==0 and i%5==0: 
                sum=sum+i
        print("sum of 4 and 5 divisables of  ",sum)
        return b(a)
    return inner
@sayed
    
def b(a):
    print("")
b(101)   