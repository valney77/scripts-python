from random import randint
from os import system
from time import sleep

system('clear')

print ('''
____  __  ______ ___  ___  _________     ____/ /___ _
  / __ \/ / / / __ `__ \/ _ \/ ___/ __ \   / __  / __ `/
 / / / / /_/ / / / / / /  __/ /  / /_/ /  / /_/ / /_/ /
/_/ /_/\__,_/_/ /_/ /_/\___/_/   \____/   \__,_/\__,_/
   _________  _____/ /____
  / ___/ __ \/ ___/ __/ _ l
 (__  ) /_/ / /  / /_/  __/
/____/\____/_/   \__/\___/\n\n''')
numero = int(input('digite quantos numero vai precisar numero : ').center(50))
contador = 0

for contador in range(1, numero +1):

    numero_sorte = randint(1,100)
    sleep(5)
    print ('--------------',numero_sorte,'--------------')
