def divisione(a,b):
    return a/b

def somma(a,b):
    return a+b

def sottrazione(a,b):
    return a-b

def moltiplicazione(a,b):
    return a*b

print('''Ciao, sono la calcolatrice!
 dimmi che operazione vuoi fare:
      A= Addizione
      B= Sottrazione
      C= Moltiplicazione
      D= Divisione
      ''')
scelta=input("scrivi qui: ")
scelta = scelta.upper()


if (scelta=="A"):


    # faccio la somma
    print("dimmi due numeri: ")
    a=int(input("primo numero: "))
    b=int(input("secondo numero: "))
    print(somma(a,b))

elif scelta=="B":
    # faccio la sottr
    print("dimmi due numeri: ")
    a = int(input("primo numero: "))
    b = int(input("secondo numero: "))
    print(sottrazione(a, b))

elif scelta=="C":
    # faccio la moltipl
    print("dimmi due numeri: ")
    a = int(input("primo numero: "))
    b = int(input("secondo numero: "))
    print(moltiplicazione(a, b))

elif scelta=="D":
    #faccio la divis
    print("dimmi due numeri: ")
    a = int(input("primo numero: "))
    b = int(input("secondo numero: "))
    while b==0:
        b= int(input("con 0 non posso! scegli un altro numero!: "))
    print(divisione(a, b))
else:
    print("non hai inserito un'operazione valida")


print("grazie e arrivederci!")
