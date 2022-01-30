import random

#Uvítání
print("Znáš hru Kámen, nůžky, papír? Pojďme si zahrat.")
print("Zadej 'kámen', 'nůžky' nebo 'papír'. Slova zadávej malými písmeny a s diakritikou.")
print("Zadáním slova 'konec', program ukončuje hru.")


vyber_pocitace = ["kámen", "nůžky", "papír"]
tah_pocitace = random.choice(vyber_pocitace)

#funkce hry Kámen, Nůžky a Papír
def hra():

    while True:

        tah_hrace = input("Tvůj tah: ").strip()

        # Zkontrolovat tah hrace
        # Kdyz hrac napise 'konec' funkce vrati 'false'
        if tah_hrace == "konec":
            print('Škoda. Třeba se uvídíme příště')
            return False
           

        if tah_hrace == "kámen":
            if tah_pocitace == "kámen":
                print("Tah počítače: ", tah_pocitace, "\nRemíza!")
            elif tah_pocitace == "nůžky":
                print("Tah počítače: ", tah_pocitace,"\nVyhrál jsi!")
            else: 
                print("Tah počítače: ", tah_pocitace,"\nProhrál jsi!")
           

        elif tah_hrace == "nůžky":
            if tah_pocitace == "kámen":
                print("Tah počítače: ", tah_pocitace, "\nProhrál jsi!")
            elif tah_pocitace == "nůžky":
                print("Tah počítače: ", tah_pocitace, "\nRemíza!")
            else: 
                print("Tah počítače: ", tah_pocitace, "\nVyhrál jsi!")
            

        elif tah_hrace == "papír":
            if tah_pocitace == "kámen":
                print("Tah počítače: ", tah_pocitace, "\nVyhrál jsi!")
            elif tah_pocitace == "nůžky":
                print("Tah počítače: ", tah_pocitace, "\nProhrál jsi!")
            else: 
                print("Tah počítače: ", tah_pocitace, "\nRemíza!")
            
        else:
            print("Zadej jen kámen, nůžky nebo papír.")
            

hra()