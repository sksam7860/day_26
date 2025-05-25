def sayed(b):
    def inner(a):
        sum=0
        for i in range(a+1):
            if i%3==0 and i%4==0: 
                sum=sum+i
        print("sum of 3and 4 divisibles of  ",sum)
        return b(a)
    return inner
@sayed
    
def b(a):
    print("")
b(101)   