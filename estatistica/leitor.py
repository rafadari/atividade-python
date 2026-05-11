import csv

def converter(valor):
    try:
        return int(valor)
    except:
        pass

    try:
        return float(valor)
    except:
        pass

    return valor


def ler_csv(caminho):
    dados = []

    with open(caminho, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha_convertida = {}

            for chave, valor in linha.items():
                linha_convertida[chave] = converter(valor)

            dados.append(linha_convertida)

    return dados