n=int(input())
def fact(n):
    if n==0:
        return 1
    else:
        n*fact(n-1)
print(fact(n))
