maiuscula = 0
minuscula = 0
numeros = 0
branco = 0
n = 0
with open('texto.txt','r') as arquivo:
    texto = arquivo.readlines() # Vai transformar em uma lista cada linha e guardar em texto

    n = (len(texto) -1) # e ira computar quantas linhas terá, como é quebra de linhas sera (num de linhas - 1)

    for i,palavras in enumerate(texto): # Primeiro for para acessar cada item da lista 
        for letra in palavras: # Segundo for para acessar cada letra de cada palavra
            if letra.isupper():
                maiuscula += 1
            elif letra.islower():
                minuscula += 1
            elif letra in ['0','1','2','3','4','5','6','7','8','9']:
                numeros += 1
            elif letra.isspace():
                branco += 1   
        # n += 1 Nao sei se ficaria utilizar aqui no for ou com len acima
print(f'Tivemos {maiuscula} letras maiusculas, {minuscula} letras minusculas, {branco} espaços em branco, {numeros} numeros e {n} quebras de linhas')

# Feedback por favor:
# Professor sou novo em python e estou adorando a facilidade em escrever o codigo, gostaria de saber se teria um jeito melhor em escrever o 
# codigo pois tentei identifcar a quebra de linha com letra == '\n' em apenas um for e nao foi identificada, ela nao entrava no if, desde já grato