a,b = int(input("nr1= ")),int(input("nr2= "))

def suma(a,b):
    return a+b

print("Suma= ",suma(a,b))

def produs(a,b):
    return a*b

print("Produsul= ",produs(a,b))

def media(a,b):
    return (a+b)/2

print("Media aritmetica= ",media(a,b))

c=[]
def max_div(a, b):
    n=0
    for i in range(1, min(a, b)+1):
        if a%i==b%i==0:
            n+=1
            c.append(i)
max_div(a, b)

print("Cel mai mare divizor comun= ",c[-1])

d=[]
def min_mult(a, b):
    return (a * b) // c[-1]

print("Cel mai mic multiplu comun= ",min_mult(a, b))

print("Numarul minim= ",min(a,b))

print("Numarul maxim= ",max(a,b))

def suma_f():
    a,b = int(input("nr1= ")),int(input("nr2= "))
    print(a+b)

suma_f()

def produs_f():
    a,b = int(input("nr1= ")),int(input("nr2= "))
    print(a*b)

produs_f()

print("Toti divizorii comuni: ",end="")
print(*c,sep=' ; ')

m=[]
def mult_com_5(a,b):
    x=a*b
    for i in range(5):
        m.append(x)
        x=x*2
mult_com_5(a,b)

print("Cinci multipli comuni: ",end="")
print(*m,sep=' ; ')

list_a,list_b=[],[]
def comun(a,b):
    list_a.append([int(x) for x in str(a)])
    list_b.append([int(x) for x in str(b)])
    c=[*set([x for x in str(a) if x in str(b)])]
    p=[*set([x for x in str(a) if x not in str(b)])]
    c.sort();p.sort()
    return c,p

print("Cifrele comune: ",end="")
print(*(comun(a,b)[0]),sep=' ; ')

print("Cifrele care se regasesc doar in primul numar: ",end="")
print(*(comun(a,b)[1]),sep=' ; ')

def nr_div(n):
    c=[]
    for i in range(1,n+1):
        if n%i==0:
            c.append(i)
    return(len(c))

if nr_div(a)==nr_div(b):
    print("PRIETENE")
