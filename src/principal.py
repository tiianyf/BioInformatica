import DNA


def main():
    sequencia = "GCAAAGACGCTGACCAA"
    sequencia = list(sequencia)
    dna = DNA()
    dna.calcular_distancia(sequencia, 8)


if __name__ == '__main__':
    main()
