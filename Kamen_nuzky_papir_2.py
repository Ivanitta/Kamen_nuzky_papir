import random


#funkce hry
def hrame_hru():
  vyber = ["kamen","papir","nuzky","kámen","papír","nůžky"]
  vyber_pocitace =["kámen","papír","nůžky"]


  print("Zahráme si Kámen, nůžky, papír.")
  print("Zadáním slova 'konec', program ukončuje hru.")

  while True:
    #hráč
    hrac=input("Zadej svůj tah:").lower()

    #počítač
    pocitac=random.choice(vyber_pocitace)
    print(f"Počítač vybral,{pocitac}")
      
    if hrac == "konec":
      print("Děkuji za hru. Někdy příště")
      return False


    if hrac not in vyber and hrac != "konec" :
      print("Jen kámen, papír nebo nůžky.")
    elif hrac == pocitac:
      print("Remíza")
    elif ((hrac=="kamen" or hrac=="kámen") and pocitac=="nůžky") or \
      ((hrac=="papir" or hrac=="papír") and pocitac=="kámen") or \
      ((hrac=="nuzky" or hrac=="nůžky") and pocitac=="papír"):
      print("Vyhrál jsi.")
    else:
      print("Prohrál jsi.")


hrame_hru()