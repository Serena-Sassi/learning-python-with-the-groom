def divisione(a,b):
    return a/b

def somma(a,b):
    return a+b

def sottrazione(a,b):
    return a-b

def moltiplicazione(a,b):
    return a*b

def procedura_input():
    print("dimmi due numeri: ")
    a = int(input("primo numero: "))
    b = int(input("secondo numero: "))
    return a,b
continua = True

while continua:

    print('''Ciao, sono la calcolatrice!
     dimmi che operazione vuoi fare:
          A= Addizione
          B= Sottrazione
          C= Moltiplicazione
          D= Divisione
          ESCI= Esci
          ''')
    scelta=input("scrivi qui: ")
    scelta = scelta.upper()


    if (scelta=="A"):


        # faccio la somma
        a,b=procedura_input()
        print(somma(a,b))

    elif scelta=="B":
        # faccio la sottr
        a, b = procedura_input()
        print(sottrazione(a, b))

    elif scelta=="C":
        # faccio la moltipl
        a,b=procedura_input()
        print(moltiplicazione(a, b))

    elif scelta=="D":
        #faccio la divis
        a,b=procedura_input()
        while b==0:
            b= int(input("con 0 non posso! scegli un altro numero!: "))
        print(divisione(a, b))
    else:
        print("non hai inserito un'operazione valida")

    scelta=input("desideri fare altro? S=Si, altro=Esci: ")
    scelta=scelta.upper()

    if scelta!= "S":
        continua=False




print("grazie e arrivederci!")
