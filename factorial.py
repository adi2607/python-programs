def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
num=5
r=factorial(num)
print(f"the factorial number of {num} is {r}")