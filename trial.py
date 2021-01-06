n=int(input())

def fact(n):
    if n==0:
        return 1
    else:
        n*fact(n-1)

for i in range(n):
    print(n-i)
print("Blast off!!")
print(fact(n))
