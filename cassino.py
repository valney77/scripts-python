from random import randint
from time import sleep
from os import system


System('clear')

#cores
blue = '\033[40;05;35m'
red = '\033[40;05;31m'
green = '\033[40;05;32m'
cyan = '\033[40;05;30m'
print (blue+'''__
  _________  / /___  ______________ ______
 / ___/ __ \/ / __ \/ ___/ ___/ __ `/ ___/
/ /__/ /_/ / / /_/ / /  / /__/ /_/ (__  )
\___/\____/_/\____/_/   \___/\__,_/____/ ''')

while True:

    nc = randint(1,90)
    pas = randint(1,2)

    if pas == 1:
        sleep(3)
        print (red+'\n##vermelho##'.center(50))
    elif pas == 2:
        sleep(3)
        print (cyan+'\n##preto##'.center(50))
    elif nc == 3:
        sleep(3)
        print (green+'\n##verde##'.center(50))

#POWERED BY 2M

#SCRIPT PARA TESTE DE ACERTOS EM JOGOS.
