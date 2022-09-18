from os import system

systen('clear')

try:
    while True:

        print ('''+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
|c|a|l|c|u|l|a|d|o|r|a| |p|y|t|h|o|n|
+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+'''\n\n)
        operador = int(input('[1]adiçao\n[2]subtração\n[3]multiplicação\n[4]divisão\n[5]sair\n»»'))
        if (operador == 5):
            print ('saiu com sucesso!')
            break
        num=float(input('digite um numero:'))
        num_du=float(input('digite outro numero:'))
        print ('calculando...'.center(50))

        if (operador==1):
            ad=num+num_du
            print ('\n##{}+{}={}##\n'.format(num,num_du,ad))
        elif (operador==2):
            sb=num-num_du
            print ('\n##{}-{}={}##\n'.format(num,num_du,sb))
        elif (operador==3):
            mp=num*num_du
            print ('\n##{}×{}={}##\n'.format(num,num_du,mp))
        elif (operador==4):
            dv=num/num_du
            print ('\n##{}÷{}={}##\n'.format(num,num_du,dv))
except ValueError:
    print ('digite uma entrada valida'.center(50))

# powered by :2M date:12/09/2020
