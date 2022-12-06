# liste

lista = [9.83, "pasta", 22, 44, 1.2]
print(type(lista))
print(lista)


lista2 = ["amore", "pizza", "luna", lista] 
print(lista2)  # per unire le due liste

print(lista[1])  # per far risaltare solo il valore 1
print(lista[-1])  # ultimo elemento

print(lista2[3][2])  # elemento di una lista in una lista

primi = [2,3,5,7,11,13,17,23,29,31,37,41,43,47]
print(primi[4:10])
fetta = primi[4:10]
print(fetta)

primi[4:]  # numeri a partire dall'elemento 4

primi[:5]  # numeri dall'inizio fino al valore 5

primi = [2,3,5,7,11,13,17,23,29,31,37,41,43,47]
match = 11  # avvisa se nella lista è presente il numero di match

for el in primi:
    if el == match:
        output = str(el) + " == " + str(match)
        print( "Match!" + output)
    else:
        print(el)

# metodi delle liste

spesa = ["pasta","pollo", "mele"]
spesa += "sapone"  # lista dei singoli caratteri
print(spesa)

# metodo = tipo_di_dato.nome_metodo(eventiali_parametri)

spesa.append("sapone")  # per aggiungere correttamente elementi alla lista
print(spesa)

spesa_extra = ["carote", "uova", "riso"]
spesa.extend(spesa_extra)  # aggiungere una lista in una lista
print(spesa)


alfabeto = ["d", "b","a","c"]
alfabeto.sort()  # per ordinare gli elementi di una lista
print(alfabeto) 

numeri = [2,4,3,6,5,1]
numeri.sort(reverse=True)  # per ordinarli in ordine 
print(numeri)

# indici
numeri = [2,4,3,6,5,1,56]
print(numeri.index(56))  # per visualizzare l'indice del numero selezionato

# sostituire un valore in una lista

spesa = ["pasta","pollo", "mele"]
spesa[1] = "tacchino"
print(spesa)

# rimuovere elementi da una lista
del spesa[0]
print(spesa)

lista1 = [True, None, "poker", 2.34, 1976]
lista1.pop()
print(lista1)  # rimuove solo l'ultimo elemento
# oppure
lista1.remove(None)  # rimuove il valore selezionato
print(lista1)


