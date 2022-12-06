def polite_greeting():
    print("Greetings my fellow!")

def smile():
    print(":)")


def say_my_name():
    name = input("Come ti chiami? ")
    print("Il tuo nome è: ", name)

say_my_name()
    

def addizione(a, b):
    print("Questa è a funzione addizione.")
    risultato = a + b
    print("Il risultato è ", str(risultato))

addizione(15, 5)

# oppure Return

def addizione(a, b):
    risultato = a + b
    return risultato

risultato = addizione(3, 3)
print(risultato)
print(addizione(21,9))

def laptop_nuovo(ram, CPU, antivirus = False):
    print("Il laptop nuovo avrà le seguenti caratteristiche: ")
    print("RAM:  " + ram)
    print("CPU: " + CPU)
    if antivirus == True:
        print(" Ha comprato anche l'antivirus")

laptop_nuovo("16GB", "I7", antivirus = True)






