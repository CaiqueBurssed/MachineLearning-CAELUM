import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home, como_funciona, contato, comprou in leitor:

        dado = [int(home), int(como_funciona), int(contato)]

        X.append(dado)
        Y.append(int(comprou))

    return X, Y


X, Y = carregar_acessos()

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(X, Y)

resultado = modelo.predict(X)

diferencas = resultado - Y

acertos = [d for d in diferencas if d == 0]

total_acertos = len(acertos)
total_elementos = len(X)

taxa_acerto = 100.0 * total_acertos / total_elementos

print(taxa_acerto)
print(total_elementos)
