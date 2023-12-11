from random import randint
from time import time
cont = 0
senha = -1
qSenha = -1
inicioExecucao = time()

while senha == -1:
    senha = int(input("Digite senha de seis digitos\n"))
    if senha >-1 and senha < 1000000:
        while senha != qSenha:
            qSenha = randint(0,999999)
            cont=cont+1
        print ("\nSenha digitada: " + str(senha))
        print ("\nTentativas ate quabrar senha: " + str(cont))
        fimExecucao = time()
        tempoExecucao = fimExecucao - inicioExecucao
        print ("\nTempo de tentativa, em segundos: " + str(tempoExecucao))
        print ("\nTentativas por segundo: " + str(cont/tempoExecucao))
    else:
        print ("Rode o programa novamente, digiando senha de seis digitos")