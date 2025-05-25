for x in range(2,101):
    factors=0
    for y in range(1,1+x):
        if x%y==0:
            factors=factors+1
    if factors==2:
        print(x)
        if True:
            print(x)
    else:
         print("")    
