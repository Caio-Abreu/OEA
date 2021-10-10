from io import SEEK_SET
from struct import Struct
import os


registroCEP = Struct("72s72s72s72s2s8s2s")

def main():
    caminho = "cep.dat"
    size_file = os.stat(caminho).st_size
    tamanhoDaLinha = registroCEP.size
    numeroDelinhas = size_file // registroCEP.size
    numeroDivisoes = int(input("Numero de divisoes que deseja: "))
    while(numeroDivisoes % 2):
        print('O numero de divisões precisa ser um número par !!!')
        numeroDivisoes = int(input("Numero de divisoes que deseja: "))
    qtdLinhaPorDivisao = numeroDelinhas // numeroDivisoes 
    versao = 0
    with open(caminho,"rb") as arquivo: 
        for divisaoAtual in range(1, numeroDivisoes+1):
            listaTemp= []
            arquivo.seek((divisaoAtual-1) * qtdLinhaPorDivisao * tamanhoDaLinha, SEEK_SET) 
            line = arquivo.readline(tamanhoDaLinha)
            i = 1

            while(i <= qtdLinhaPorDivisao) and len(line)>0:
                endereco = registroCEP.unpack(line) 
                listaTemp.append(endereco) 
                line = arquivo.read(tamanhoDaLinha)
                i += 1
            
            listaTemp.sort(key=lambda e: e[5]) 
            with open("ordenada{}_{}.dat".format(versao, divisaoAtual),"wb") as file:
                for endereco in listaTemp: 
                    file.write(registroCEP.pack(*endereco))

    agrupa(numeroDivisoes, versao)
    print("Processo finalizado!!!")

def agrupa(qtdDeArquivos, versao):
    while(qtdDeArquivos!=1 ):
        limit = qtdDeArquivos
        divisaoAtual = 1
        j = 1
        while(divisaoAtual <= limit):
            caminhoArquivo1 ="ordenada{}_{}.dat".format(versao, divisaoAtual) 
            caminhoArquivo2 = "ordenada{}_{}.dat".format(versao, divisaoAtual+1)
            intercala(caminhoArquivo1, caminhoArquivo2,versao+1, j)
            divisaoAtual+=2
            j+=1
        versao += 1
        qtdDeArquivos /= 2

def intercala(arquivo1, arquivo2, versionIntercala, file_id):
    with open(arquivo1, "rb") as f1, open(arquivo2, "rb") as f2:

        novo_arquivo = open("ordenada{}_{}.dat".format(versionIntercala, file_id), "wb")
        line1 = f1.read(registroCEP.size)
        line2 = f2.read(registroCEP.size)
        

        while((len(line1) > 0 and len(line2) > 0)):
            endereco1 = registroCEP.unpack(line1)
            endereco2 = registroCEP.unpack(line2)
            cep1 = endereco1[5]
            cep2 = endereco2[5]

            if(cep1 < cep2):
               novo_arquivo.write(registroCEP.pack(*endereco1))
               line1 = f1.read(registroCEP.size)
            else:
                novo_arquivo.write(registroCEP.pack(*endereco2))
                line2 = f2.read(registroCEP.size)
        
        while(len(line1)>0):
            endereco1 = registroCEP.unpack(line1)
            novo_arquivo.write(registroCEP.pack(*endereco1))
            line1 = f1.read(registroCEP.size)
        while(len(line2)>0):
            endereco2 = registroCEP.unpack(line2)
            novo_arquivo.write(registroCEP.pack(*endereco2))
            line2 = f2.read(registroCEP.size)
        novo_arquivo.close()
    excluir(arquivo1,arquivo2)

def excluir(file1,file2):
    os.remove(file1)
    os.remove(file2)

main()