import numpy as np
lista=list(np.random.randint(0,10,30))
lista=[2,3,2,2,2,3,4,1,2,3,4]

## {0,1,2,...,d}

## modulo q... %q
## h=d**(m-1)%q

wzorzec=[2,3,4]

m=len(wzorzec)
n=len(lista)

w=0
for i in range(m):
    w=w*10+wzorzec[i]

t0=0
for i in range(m):
    t0=t0*10+lista[i]

# t0=232

index=0
for i in range(n-m):
    if w==t0:
        if wzorzec==lista[0:m]:
            index+=1
            t0=((t0-lista[i]*10**(m-1))*10+lista[i+m])

    if w==t0:
        if wzorzec==lista[i+1:i+m+1]:
            index+=1
            print(lista[1+i:1+i+m])

print(index)
