def estatisticas(dados, campo):

    valores = []

    for linha in dados:
        valor = linha[campo]

        if isinstance(valor, (int, float)):
            valores.append(valor)

    total = sum(valores)

    return {
        "media": total / len(valores),
        "minimo": min(valores),
        "maximo": max(valores),
        "total": total
    }