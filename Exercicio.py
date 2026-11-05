def resolver(sequencia):
    n = len(sequencia)
    tabela = [1] * n

    for i in range(1, n):
        for j in range(i):
            if sequencia[j] < sequencia[i]:
                tabela[i] = max(tabela[i], tabela[j] + 1)

    return max(tabela)


sequencia = [10, 22, 9, 33, 21, 50, 41, 60]
resultado = resolver(sequencia)
print("Resultado:", resultado)
