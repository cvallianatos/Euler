def isPrime(x):
    c=0
    for i in range(1,x+1):
        if(x%i==0):
            c+=1
    if(c==2):
        return True
    return False
        
def genPrimeList(n):
    x=[]
    for i in range(0,n):
        if isPrime(i):
            x.append(i)
    return x

n=int(input())
x=genPrimeList(n)
init=0
c=-1
for i in x:
      init=init+i
      if(init<n and isPrime(init)):
              c+=1

print(c)