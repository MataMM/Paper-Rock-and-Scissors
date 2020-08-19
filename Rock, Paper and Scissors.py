import random
import sys

##Embellecedor  0: Piedra || 1: Papel || 2: Tijeras
print("0)Piedra")
print("1)Papel")
print("2)Tijeras")

## Variables Y varios
playerchoice = int(input("Elección: ")) ## 0/0 empate //  1/0 gana // 2/0 pierde 1/2
botchoice = random.randint(0, 2)
botchoice2 = botchoice ##Esto es para embellecer.

if botchoice2 == 0:
    botchoice2  = "Piedra"
elif botchoice2 == 1:
    botchoice2 = "Papel"
else:
    botchoice2 = "Tijeras"

##Extra
if playerchoice >= 3:
    print("Por gracioso te voy a cerrar el programa.")
    sys.exit()
else:
    None

##Decisiones de ganador
if playerchoice == botchoice: #Han es cogido los dos lo mismo. 
    print("Empate.")
    print("La elección del bot fue",botchoice2)
    sys.exit()
elif playerchoice == 1 and botchoice == 0 : #Jugador gana (Papel vs Piedra)
    print("Jugador gana.")
    print("La elección del bot fue",botchoice2)
    sys.exit()
elif  playerchoice == 0 and botchoice == 1: #Bot gana (Papel vs Piedra)
    print("Bot gana.")
    print("La elección del bot fue",botchoice2)
    sys.exit()
elif playerchoice == 0 and botchoice == 2: #Jugador gana (Piedra vs Tijeras)              
    print("Jugador gana.")
    print("La elección del bot fue",botchoice2)
    sys.exit()
elif  playerchoice == 2 and botchoice == 0: #Bot gana (Piedra vs Tijeras)
    print("Bot gana.")
    print("La elección del bot fue",botchoice2)
    sys.exit()
elif playerchoice == 2 and botchoice == 1: #Jugador gana (Papel vs Tijeras)
    print("Jugador gana.")
    print("La elección del bot fue",botchoice2)
    sys.exit()
elif playerchoice == 1 and botchoice == 2: #Bot gana (Papel vs Tijeras)
    print("Bot gana.")
    print("La elección del bot fue",botchoice2)
    sys.exit()
else: 
    None
    print("Falla en el sistema")
    sys.exit()
