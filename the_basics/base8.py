# variabili globali e locali

x = 15  # variabile globale

def funzione():
    global x
    x += 2 
    return x
print(funzione())


def funzione2():
    x = 24
    return x

new_val = funzione2() + 6
print(new_val)


