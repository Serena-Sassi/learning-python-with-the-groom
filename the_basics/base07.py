potito = [7, 2, 39999, 68, 1, 0, 509, 77, 9]

ditino = 0  # ditino parte da zero perchè indico il primo numero della lista
big = potito[0]  # il numero più grande che conosco fino ad ora è il primo che vedo
while ditino < len(potito):  # mentre il ditino è minore della lunghezza della lista
    if big < potito[ditino]:  # controllo che il numero più grande che conosco sia minore del numero che sto indicando
        big = potito[ditino]  # se è vero il big diventa il numero che sto indicando al momento
    ditino = ditino+1  # sposto il ditino in avanti
print(big)  # stampo il numero più grande che conosco a fine lista
