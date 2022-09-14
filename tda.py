#ex1
def ex1():
    s=0
    for i in range(9):
        if i%2==0:
            s=s+0.5**i
    return(s)
print("S = ", ex1())
dict=0

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return(fact)

#ex2
n=int(input("Introducet n: "))
m=int(input("Introducet m: "))
c=fact(n)/(fact(m)*fact(n-m))
print("C = ", c)

def simplificare_frac(numar, numit):
    i = 2
    while i < min(numar, numit) + 1:
        if (numar % i == 0) and (numit % i == 0):
            numar = numar // i
            numit = numit // i
        else:
            i += 1
    return (int(numar), int(numit))

def adunare_frac(n1, n2):
    n=n1[1]*n2[1]
    n1[0]=n1[0]*n/n1[1]
    n2[0]=n2[0]*n/n2[1]
    n1[1]=n2[1]=n
    numar=n1[0]+n2[0]
    numit=n
    return (numar, numit)

#ex3
f1 = list(eval(input("Introduceti prima fractie: ")))
f2 = list(eval(input("Introduceti a doua fractie: ")))
ad=adunare_frac(f1, f2)
print("Suma fractiilor = ", simplificare_frac(ad[0], ad[1]))

def inm_frac(n1,n2):
    numar=n1[0]*n2[0]
    numit=n1[1]*n2[1]
    return(numar, numit)

#ex4
inm=inm_frac(f1, f2)
print("Produsul fractiilor = ", simplificare_frac(inm[0], inm[1]))
