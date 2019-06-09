from random import randint, randrange


class DNA(object):

    @staticmethod
    def criar_sequencia_aleatoria(k):
        """
        Retorna uma sequencia(lista) aleatória de tamanho k
        :param k: tamanho (length) da sequencia desejada
        :rtype: list()
        :return lista de sequencia aleatoria
        """

        sequencia = []
        letra = str

        for i in range(k):
            random = randint(1, 4)
            if random == 1:
                letra = 'A'
            elif random == 2:
                letra = 'T'
            elif random == 3:
                letra = 'G'
            elif random == 4:
                letra = 'C'
            sequencia.append(letra)

        return sequencia

    @staticmethod
    def calcular_erros(trecho, sequencia, k):
        """
        Calcula a quantidade de erros (mutações) de um trecho em relação a
        sequencia original de tamanho k
        :param trecho:
        :param sequencia:
        :param k:
        :return:
        """

        erros = 0
        for i in range(k):
            if trecho[i] != sequencia[i]:
                erros += 1
        return erros

    def percorrer(self, sequencia, trecho, k):
        """
        Slice and Switch
        Percorre a sequencia original
        :rtype: int
        """

        numero_de_erros = []
        numero_de_pulos = len(sequencia) - k + 1

        for i in range(numero_de_pulos):
            comparador = sequencia[i: i + k]
            numero_de_erros.append(self.calcular_erros(trecho, comparador, k))
        return numero_de_erros

    def calcular_distancia(self, sequencia, k):
        trecho = self.criar_sequencia_aleatoria(k)
        print("\nTamanho do trecho: ", len(trecho))

        trecho = list(trecho)
        distancia = min(self.percorrer(trecho, sequencia, k))

        print(f"Trecho aleatório: {''.join(trecho)}")
        print(f"sequencia: {''.join(sequencia)}")
        print(f"A menor distância é {distancia}")

        return distancia

    def criar_motif(self, linha, coluna):
        """
        Cria o motif (matriz contendo várias sequencias aleatórias de motif).
        :param linha: quantidade de sequencias
        :param coluna: tamanho (length) das sequencias
        :return: a matriz de motif
        """

        motif = []

        for i in range(linha):
            sequencia = self.criar_sequencia_aleatoria(coluna)
            motif.append(sequencia)

        return motif

    @staticmethod
    def profile_frequencia(motif):
        """
        Calcula a frequencia e cria o profile (matriz com a criar_frequencia),
        retornando-o.
        :param motif: a matriz de motif
        :rtype: matriz contendo a frequencia absoluta
        """

        linhas = len(motif)
        colunas = len(motif[0])
        profile = [[], [], [], []]

        # zerando a matriz de resultados
        for i in range(4):
            for j in range(colunas):
                profile[i].append(0)

        for i in range(colunas):
            for j in range(linhas):
                if motif[j][i] == 'A':
                    profile[0][i] += 1

                elif motif[j][i] == 'C':
                    profile[1][i] += 1

                elif motif[j][i] == 'G':
                    profile[2][i] += 1

                elif motif[j][i] == 'T':
                    profile[3][i] += 1

        return profile

    @staticmethod
    def criar_sequencia_provavel(profile):
        """
        A partir de determinado profile (matriz de frequencia), calcular a
        sequencia mais provavel.
        :return uma lista de motif contendo a sequencia mais provavel
        :rtype: list
        """

        colunas = len(profile[0])
        sequencia_provavel = []

        # zerando a sequencia
        for i in range(colunas):
            sequencia_provavel.append(0)

        # calculando maior ocorrencia
        for i in range(colunas):
            maior_numero = 0

            if profile[0][i] >= maior_numero:
                maior_numero = profile[0][i]
                sequencia_provavel[i] = 'A'

            if profile[1][i] >= maior_numero:
                maior_numero = profile[1][i]
                sequencia_provavel[i] = 'C'

            if profile[2][i] >= maior_numero:
                maior_numero = profile[2][i]
                sequencia_provavel[i] = 'G'

            if profile[3][i] >= maior_numero:
                maior_numero = profile[3][i]
                sequencia_provavel[i] = 'T'

        return sequencia_provavel

    @staticmethod
    def profile_probabilidade(profile):
        """
        Transforma o profile original (matriz de frequencia) em um profile com
        as probabilidades (matriz com numeros flutuantes, utilizando
        percentagem)
        :rtype: uma matriz de profile
        """

        colunas = len(profile[0])
        soma_colunas = 0
        novo_profile = [[], [], [], []]

        # zerando matriz para novo profile, e pegando a soma das colunas
        for i in range(4):
            soma_colunas += profile[i][0]
            for j in range(colunas):
                novo_profile[i].append(0.0)

        for i in range(colunas):
            for j in range(4):
                valor = profile[j][i] / soma_colunas
                novo_profile[j][i] = valor

        return novo_profile

    @staticmethod
    def calcular_probabilidade_trecho(trecho, profile):
        """
        Dado um trecho de tamanho (len) igual a do profile, retorna a
        probabilidade de sua ocorrencia
        (com 4 casas decimais).
        :rtype: float
        """

        trecho = list(trecho)
        resultado = 1

        for i in range(len(trecho)):
            if trecho[i] == 'A':
                resultado *= profile[0][i]

            elif trecho[i] == 'C':
                resultado *= profile[1][i]

            elif trecho[i] == 'G':
                resultado *= profile[2][i]

            elif trecho[i] == 'T':
                resultado *= profile[3][i]

        return round(resultado, 4)

    @staticmethod
    def seleciona_trecho_aleatorio(k, motif):
        tam_linha = len(motif[0])
        kmers = []
        for motif in motif:
            n = randrange(tam_linha - k)
            kmers.append(motif[n:n + k])

        return kmers

    @staticmethod
    def criar_motif_de_trechos_aleatorios(motif, k):
        """
        Cria uma nova matriz de motif, com trechos selecionados aleatoriamente
        da matriz de motif anterior (passada como parametro).
        :return uma nova matriz
        :param k: o tamanho (length) do trecho aleatorio a ser gerado
        :param motif: o motif a ser analisado
        :rtype: list
        """

        linhas = len(motif)
        colunas = len(motif[0])
        motif_aleatorio = [[0] * k for i in range(linhas)]

        for i in range(linhas):
            ponto_partida_maximo = linhas - k
            inicio_random = randint(0, ponto_partida_maximo)
            trecho = motif[i][inicio_random:inicio_random + k]
            motif_aleatorio[i] = trecho

        return motif_aleatorio

    @staticmethod
    def remover_kmer_random(motif):
        """
        Dado o motif, retira uma linha aleatoriamente da matriz (deleta uma
        sequencia), e retorna o motif alterado.
        :param motif: o motif cuja linha (kmer) será retirado aleatoriamente.
        :rtype: list
        """

        linha_retirada = randint(0, len(motif))
        del (motif, motif[linha_retirada])

        return motif


def menores_distancias():
    qtd_sequencias = int(
        input("\nInsira aqui a quantidade de sequencias que deseja analisar: "))
    k = int(input("E qual será o tamanho dessas sequencias? "))
    somatorio = []

    for i in range(qtd_sequencias):
        dna = DNA()
        sequencia = dna.criar_sequencia_aleatoria(k)
        somatorio.append(dna.calcular_distancia(sequencia, k))

    print("A soma das menores distancias é: ", sum(somatorio))


def criar_matriz_de_motif():
    linha = int(input("\nInsira aqui quantas sequencias deseja analisar: "))
    coluna = int(input("\nInsira aqui o tamanho das sequencias: "))

    dna = DNA()
    motif = dna.criar_motif(linha, coluna)

    print(f"A matriz de motif é:")

    for i in range(linha):
        print(motif[i])

    return motif


def criar_profile(motif):
    profile = DNA.profile_frequencia(motif)

    print(f"A = ", profile[0])
    print(f"C = ", profile[1])
    print(f"G = ", profile[2])
    print(f"T = ", profile[3])

    return profile


def calcular_probabilidade_sequencia(sequencia, profile):
    """
        Dado um código genético (sequencia), calcular qual a probabilidade de
        cada trecho de tamanho kmer, se analisado o profile.
        :param sequencia: o codigo genetico em si
        :param profile: o profile da sequencia
    """
    k = int(input("Qual é o tamanho dos trechos que serão analisados? "))
    numero_de_pulos = len(sequencia) - k + 1

    for i in range(numero_de_pulos):
        trecho = sequencia[i: i + k]
        prob = DNA.calcular_probabilidade_trecho(trecho, profile)
        print(f"O trecho é {trecho} e a probabilidade é {prob}")


def randomized_motif_search(motif):
    """
    Algoritmo de busca de motifs aleatório
    :param motif: o motif (matriz contendo várias sequencias de DNA).
    :return:
    """

    k = int(input("\nQual será o tamanho do trecho (k)? "))

    random_motif = DNA.criar_motif_de_trechos_aleatorios(motif, k)
    # random_motif = [
    #     ['T', 'A', 'A', 'C'],
    #     ['G', 'T', 'C', 'T'],
    #     ['C', 'C', 'G', 'G'],
    #     ['A', 'C', 'T', 'A'],
    #     ['A', 'G', 'G', 'T']
    # ]

    profile = DNA.profile_frequencia(random_motif)
    profile = DNA.profile_probabilidade(profile)

    qtd_linhas = len(motif)
    qtd_colunas = len(motif[0])
    numero_de_pulos = qtd_colunas - k + 1
    dict_resultados = {}
    melhor_trecho = ''
    melhor_motif = []

    for i in range(qtd_linhas):
        maior_prob = 0
        for j in range(numero_de_pulos):

            trecho = motif[i][j:j + k]
            trecho = ''.join(trecho)
            float_prob = DNA.calcular_probabilidade_trecho(trecho, profile)
            dict_resultados[trecho] = float_prob

            if float_prob > maior_prob:
                maior_prob = float_prob
                melhor_trecho = trecho

        melhor_motif.append(melhor_trecho)

    # print(melhor_motif)
    return melhor_motif


def gibbs_sampler(motif):
    # remove linha do motif (sequencia) aleatoriamente
    pass


def main():
    motif_1 = [
        ['T', 'C', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'T'],
        ['C', 'C', 'G', 'G', 'T', 'G', 'A', 'C', 'T', 'T', 'A', 'C'],
        ['A', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'T', 'T', 'C'],
        ['T', 'T', 'G', 'G', 'G', 'G', 'A', 'C', 'T', 'T', 'T', 'T'],
        ['A', 'A', 'G', 'G', 'G', 'G', 'A', 'C', 'T', 'T', 'C', 'C'],
        ['T', 'T', 'G', 'G', 'G', 'G', 'A', 'C', 'T', 'T', 'C', 'C'],
        ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'C', 'A', 'T'],
        ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'C', 'C', 'T'],
        ['T', 'A', 'G', 'G', 'G', 'G', 'A', 'A', 'C', 'T', 'A', 'C'],
        ['T', 'C', 'G', 'G', 'G', 'T', 'A', 'T', 'A', 'A', 'C', 'C']
    ]

    motif_2 = [
        ['A', 'T', 'C', 'C', 'C', 'T'],
        ['C', 'A', 'C', 'G', 'A', 'T'],
        ['A', 'A', 'C', 'C', 'C', 'T'],
        ['G', 'A', 'A', 'G', 'T', 'T'],
        ['A', 'A', 'C', 'C', 'C', 'T'],
        ['T', 'A', 'A', 'C', 'G', 'T'],
        ['A', 'A', 'G', 'G', 'G', 'T'],
        ['G', 'A', 'A', 'C', 'T', 'G']
    ]

    motif_3 = [
        ['T', 'T', 'A', 'C', 'C', 'T', 'T', 'A', 'A', 'C'],
        ['G', 'A', 'T', 'G', 'T', 'C', 'T', 'G', 'T', 'C'],
        ['C', 'C', 'G', 'G', 'C', 'G', 'T', 'T', 'A', 'G'],
        ['C', 'A', 'C', 'T', 'A', 'A', 'C', 'G', 'A', 'G'],
        ['C', 'G', 'T', 'C', 'A', 'G', 'A', 'G', 'G', 'T']
    ]

    motif_4 = [
        ['T', 'T', 'A', 'C', 'C', 'T', 'T', 'A', 'A', 'C'],
        ['G', 'A', 'T', 'A', 'T', 'C', 'T', 'G', 'T', 'C'],
        ['A', 'C', 'G', 'G', 'C', 'G', 'T', 'T', 'C', 'G'],
        ['C', 'C', 'C', 'T', 'A', 'A', 'A', 'G', 'A', 'G'],
        ['C', 'G', 'T', 'C', 'A', 'G', 'A', 'G', 'G', 'T']
    ]

    # randomized_motif_search(motif_4)

    motif_5 = [
        ['T', 'A', 'A', 'C'],
        ['G', 'T', 'C', 'T'],
        ['C', 'C', 'G', 'G'],
        ['A', 'C', 'T', 'A'],
        ['A', 'G', 'G', 'T']
    ]

    novo_motif = DNA.remover_kmer_random(motif_5)
    print(novo_motif)


if __name__ == '__main__':
    main()
