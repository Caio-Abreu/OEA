from struct import Struct
import sys

if len(sys.argv) != 2:
	print ("USO %s [CEP]" % sys.argv[0])
	quit()

registro_cep = Struct("72s72s72s72s2s8s2s")
cep = sys.argv[1]
cep_tabela_column = 5

with open('cep_ordenado.dat','rb') as arquivo:
    tamanho_linha = registro_cep.size
    arquivo.seek(0,2)
    tamanho_arquivo = arquivo.tell()
    inicio = 0
    fim = int(tamanho_arquivo/tamanho_linha)
    cont = 0
    while inicio <= fim:
        cont+=1
        meio = (inicio+fim)//2
        arquivo.seek(meio*tamanho_linha,0)
        linha = arquivo.read(tamanho_linha)
        record = registro_cep.unpack(linha)
        cep_tabela = record[cep_tabela_column].decode('latin').strip()
        if cep == cep_tabela:
            for coluna in record:
                print(str(coluna,'latin1'))
            quit()
        elif cep > cep_tabela:
            inicio = meio + 1
        else:
            fim = meio - 1

print(f"Não foi encontrado o CEP: {cep}")