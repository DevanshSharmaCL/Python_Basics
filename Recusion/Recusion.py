#recusion 

#factorial(n)= n*factorial(n-1)--------formula

def factorial(n):
    if n==0|n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(3))


#febonaci series 
#logic :
# 0,1 = (0 + 1= 1)
# 1,1 = (1 + 1 = 2)
# 2,3 = (2 + 3 = 5)
# 3,5 = (3 + 5 = 8)
# formula = f(n-1)+f(n-2)

def febonaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return febonaci(n-1) + febonaci(n-2)

print(febonaci(15))