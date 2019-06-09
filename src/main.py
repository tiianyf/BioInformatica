"""
VALOR: 35pts

1. Ler um arquivo contendo o código genético.

2. Fornecer um intervalo para os valores de K, gerando um arquivo txt para cada
   K (O intervalo será de 7 até 9).

3. O arquivo de saída deve conter (um arquivo de saída para cada K):
a) As sequências que mais se repetem e sua quantidade;
b) Quais dentre as sequências do item (a) possuem inversas e sua quantidade;
c) Acrescentar a taxa de mutação 'D', a qual permite uma quantidade 'D' de
   erros quando as comparações são feitas

OBS: Até agora é como se tivéssemos considerado tudo como D = 0.


Meu Entendimento:

-> Ler as sequencias normais que mais se repetem, ou seja, criar a funcao
pegar_sequencia(), mas somente para as sequencias normais e salvar as
sequencias mais repetidas num arquivo de texto (no caso, 3 arquivos de texto,
para k=7, k=8 e k=9)

-> Ler esse arquivo, e usar as sequencias que mais se repetem (ou melhor,
todas as sequencias que tiveram o maior número de repetições)
"""

"""
    Lê as sequências normais (não complementares) de tamanho k,
    chama a função que acha as sequências de maior repetição e salva o
    resultado em um arquivo.
"""


def ler_sequencias_e_salvar(string, k):
    numero_de_sequencias = len(string) - k + 1
    dicionario = {}

    for i in range(numero_de_sequencias):
        sequencia = string[i: i + k]

        if sequencia in dicionario:
            dicionario[sequencia] += 1
        else:
            dicionario[sequencia] = 1

    arquivo = open("../assets/resultados/sequencias_k={}.txt".format(k), "w")
    resultado = str(achar_maior_repeticao(dicionario))

    arquivo.write(resultado)
    arquivo.close()


"""
    Percorre todo o dicionário, acha as sequências com o maior número de
    repetições e retorna um novo dicionário contendo somente as
    sequências com o maior número de repetições.
"""


def achar_maior_repeticao(dicionario):
    novo_dicionario = {}
    maior_repeticao = 1

    # achando qual é a maior repetição
    for seq in dicionario:
        if dicionario[seq] > maior_repeticao:
            maior_repeticao = dicionario[seq]

    # salvando somente as sequencias com a maior repeticao no novo dicionário
    for seq in dicionario:
        if dicionario[seq] == maior_repeticao:
            if seq not in novo_dicionario:
                novo_dicionario[seq] = maior_repeticao

    return novo_dicionario


"""
    Verifica se determinada sequencia de tamanho k contém uma inversa
    complementar. Caso realmente tenha, armazene num dicionário, juntamente
    com suas possíveis repetições (dicionario[inversa] == repetição), e, por
    último, salve num arquivo.
"""


def possui_inversa(k):
    arquivo = open("../assets/dna/dna_vibrio_cholerae.txt", "r")
    string = arquivo.readline()
    arquivo.close()
    dicionario = transforma_arquivo_em_dicionario(k)
    inversas_possiveis = criando_inversas(dicionario)
    inversas_reais = {}

    # para cada letra na string
    for i in range(len(string)):
        # caso o intervalo da string esteja na lista de possíveis inversas
        # (já criada anteriormente)
        if string[i: i + k] in inversas_possiveis:
            # e se esse intervalo já foi adicionado ao dicionário de
            # 'inversas reais', adicione +1 ao seu valor (mais uma repetição)
            if string[i: i + k] in inversas_reais:
                inversas_reais[string[i: i + k]] += 1
            # caso já não tenha sido adicionada anteriormente, adicione agora
            else:
                inversas_reais[string[i: i + k]] = 1

    # depois de tudo isso, salve as 'inversas reais' num arquivo de texto
    arquivo = open("../assets/resultados/inversas_k={}.txt".format(k), "w")
    arquivo.write(str(inversas_reais))
    arquivo.close()


"""
    Abre o arquivo com as sequências e transforma em um dicionário de novo,
    para que seja fácil de manipular mais tarde.
"""


def transforma_arquivo_em_dicionario(k):
    arquivo = open("../assets/resultados/sequencias_k={}.txt".format(k), "r")
    resultado = arquivo.readline()
    arquivo.close()
    dicionario = {}

    # transformando a string em dicionário de novo (olha dentro do arquivo e
    # faz o rastreio, que fica fácil de entender)
    for i in range(len(resultado)):
        if resultado[i] == ":":
            sequencia = resultado[i - (k + 1): i - 1]
            repeticoes = resultado[i + 2]
            dicionario[sequencia] = repeticoes

    return dicionario


"""
    Lê o dicionário das sequencias que contém repetições, cria uma lista de
    "possíveis inversas", e retorna essa lista.
    O primeiro laço é feito para cada chave do dicionário (ou seja, para cada
    sequência armazenada no dicionário)
    Depois, uma string vazia é declarada
    Após isso, outro laço é chamado, percorrendo cada letra da sequência
    E a string 'troca' vai ser alterada para cada letra encontrada na minha
    sequência
    E será armazenada na minha string 'inversa'
    Após isso, a string 'inversa' será adicionada à minha lista de "possíveis
    inversas"
    Espero que, juntamente com o código, minha explicação tenha sido clara.
"""


def criando_inversas(dicionario):
    sequencias = transforma_dicionario_em_lista(dicionario)
    inversas = []

    for seq in sequencias:
        inversa = ''

        for i in seq[::-1]:  # ou 'for i in reverse(seq):'
            troca = ''
            if i == 'a':
                troca = 't'
            elif i == 't':
                troca = 'a'
            elif i == 'g':
                troca = 'c'
            elif i == 'c':
                troca = 'g'
            inversa += troca

        inversas.append(inversa)

    return inversas


"""
    Dado um dicionário, retorna uma lista com as CHAVES do dicionário.
"""


def transforma_dicionario_em_lista(dicionario):
    lista = list(dicionario)
    return lista


"""
    Achar possíveis mutações dentre as sequências, num universo da string
    original do dna.
"""


def achar_mutacao(k, d):
    arquivo = open("../assets/resultados/sequencias_k={}.txt".format(k), "r")
    seq = arquivo.readline()
    arquivo.close
    arquivo = open("../assets/dna/dna_vibrio_cholerae.txt", "r")
    dna = arquivo.readline()
    arquivo.close

    lista_seq = string_de_dicionario_para_lista(seq, k)
    numero_de_sequencias = len(dna) - k + 1

    for i in range(numero_de_sequencias):
        for seq in lista_seq:
            mutacao(dna[i: i + k], seq, k, d)


"""
    Pega a string (que está em formato de dicionário) e remove aspas,
    dois-pontos, valor etc, retornando uma lista padrão.
"""


def string_de_dicionario_para_lista(string, k):
    lista = []
    sequencia = ""

    for i in range(len(string)):
        if len(sequencia) == k:
            lista.append(sequencia)
            sequencia = ""
        if string[i].isalpha():
            sequencia += string[i]

    return lista


def mutacao(dna, seq, k, d):
    erros = 0
    for i in range(k):
        if dna[i] != seq[i]:
            erros += 1
    if erros == d:
        salvar_mutacao(seq, dna, k, d)


def salvar_mutacao(seq, dna, k, d):
    arquivo = open("../assets/resultados/mutacao_k={}_d={}.txt".format(k, d), "a+")
    resultado = "Original: " + seq + "\n Mutação: " + dna + "\n"
    arquivo.write(resultado)
    arquivo.close()


def main():
    arquivo = open("../assets/dna/dna_vibrio_cholerae.txt", "r")
    string = arquivo.readline()
    arquivo.close()

    d = int(input("\n\tInsira aqui o taxa de mutação:  "))

    for k in range(7, 10):
        ler_sequencias_e_salvar(string, k)  # somente as de maior repeticao
        possui_inversa(k)
        achar_mutacao(k, d)


if __name__ == "__main__":
    main()
