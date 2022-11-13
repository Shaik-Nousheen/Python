num = int(input("enter the number which u wanted to find the factor: "))
a=[]
if num > 0:
    for i in range(1,num + 1):
        if ( num % i) == 0:
            # print(i,"is a factor of",num) 
            a.append(i)
    print("factors of",num,"is:", a)
    highest = max(a)
    lowest = min(a)
    print("highest num is:",highest)
    print("lowest num is:", lowest)
   
