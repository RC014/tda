n,cifre,repetare2=int(input("Introduceti numarul: ")),[],[]
if n>=100000:
    print("Numarul trebuie sa fie mai mic decat 100000")
    exit()
def descompunere(x):
    cifre.append([int(i) for i in str(x)])
descompunere(n)
cifre=cifre[0]
print("a) Numarul de cifre: ",len(cifre))

def pare_imp(x):
    nr_p=[i for i in x if i%2==0]
    nr_imp=[i for i in x if i%2!=0]
    return nr_p, nr_imp

print("b) Numarul de cifre pare: ", len(pare_imp(cifre)[0]))
print("c) Numarul de cifre impare: ", len(pare_imp(cifre)[1]))

def suma(x):
    s=0
    for i in x: s+=i
    return s

print("d) Suma cifrelor: ",suma(cifre))

print("e) Cifra maxim: ",max(cifre))
print("f) Cifra minim: ",min(cifre))

print("g) Media aritmetica:", suma(cifre)/len(cifre))

def repeta2(x):
    repetare2.append([i for i in x if x.count(i)==2])
repeta2(cifre)
repetare2=[*set(repetare2[0])]
print("h) Cifrele care se repeta de 2 ori:","; ".join([str(i) for i in repetare2]))

print("i) Cifrele numarului: "," ".join([str(i) for i in cifre]))

def div(x):
    div=[]
    div.append([i for i in range(1,x+1) if x%i==0])
    return(div[0])
print("j) Divizorii numarului: ", "; ".join([str(i) for i in div(n)]))

invers = lambda x:(1/x)
print("k) Inversul numarului: ", invers(n))

cifre.sort(reverse=True)
print("l) Cel mai mare numar posibil format din aceste cifre: ", "".join([str(i) for i in cifre]))

if len(div(n))==2:
    print("m) Prim!")
