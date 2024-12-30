def fact(n):
    if (n>=0):
        if n==1 or n==0:
            return 1
        else:
             return n*fact(n-1)
    else: 

        
        return ("Invalid")
print(fact(int(input())))
print(fact(2))
