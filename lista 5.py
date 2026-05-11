#questão 1
import os
import time

caminho = input("Digite o caminho: ")

total_arquivos = 0
total_pastas = 0
tamanho_total = 0

for item in os.listdir(caminho):

    caminho_completo = os.path.join(caminho, item)

    if os.path.isfile(caminho_completo):

        total_arquivos += 1

        tamanho = os.path.getsize(caminho_completo)
        tamanho_total += tamanho

        modificacao = os.path.getmtime(caminho_completo)

        data_formatada = time.strftime(
            "%d/%m/%Y %H:%M:%S",
            time.localtime(modificacao)
        )

        print(f"Arquivo: {item}")
        print(f"Tamanho: {tamanho} bytes")
        print(f"Modificado em: {data_formatada}")
        print("-" * 30)

    elif os.path.isdir(caminho_completo):
        total_pastas += 1

        print(f"Pasta: {item}")
        print("-" * 30)

print("\nRESUMO")
print(f"Total de arquivos: {total_arquivos}")
print(f"Total de pastas: {total_pastas}")
print(f"Tamanho total dos arquivos: {tamanho_total} bytes")

#questão 3

operadores = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

def avaliar(expressao):

    expressao = expressao.replace(" ", "")

    indice = 0

    def parse_expressao():
        nonlocal indice

        resultado = parse_termo()

        while indice < len(expressao) and expressao[indice] in '+-':
            op = expressao[indice]
            indice += 1

            direito = parse_termo()

            resultado = operadores[op](resultado, direito)

        return resultado

    def parse_termo():
        nonlocal indice

        resultado = parse_fator()

        while indice < len(expressao) and expressao[indice] in '*/':
            op = expressao[indice]
            indice += 1

            direito = parse_fator()

            resultado = operadores[op](resultado, direito)

        return resultado

    def parse_fator():
        nonlocal indice

        if expressao[indice] == '(':
            indice += 1

            resultado = parse_expressao()

            indice += 1  # pula ')'

            return resultado

        inicio = indice

        while (
                indice < len(expressao)
                and (expressao[indice].isdigit() or expressao[indice] == '.')
        ):
            indice += 1

        numero = float(expressao[inicio:indice])

        return numero

    return parse_expressao()

#questão 5

import os
import zipfile

diretorio = "."

nome_zip = "backup.zip"

arquivos_txt = []

for arquivo in os.listdir(diretorio):

    if arquivo.endswith(".txt") and os.path.isfile(arquivo):
        arquivos_txt.append(arquivo)

with zipfile.ZipFile(nome_zip, "w", zipfile.ZIP_DEFLATED) as zipf:

    for arquivo in arquivos_txt:
        zipf.write(arquivo)

print("Arquivos compactados:\n")

with zipfile.ZipFile(nome_zip, "r") as zipf:

    for info in zipf.infolist():

        tamanho_original = info.file_size
        tamanho_comprimido = info.compress_size

        print(f"Arquivo: {info.filename}")
        print(f"Tamanho original: {tamanho_original} bytes")
        print(f"Tamanho comprimido: {tamanho_comprimido} bytes")
        print("-" * 30)

#questão 6

from datetime import datetime

data1 = input("Digite a primeira data (DD/MM/AAAA): ")
data2 = input("Digite a segunda data (DD/MM/AAAA): ")

d1 = datetime.strptime(data1, "%d/%m/%Y")
d2 = datetime.strptime(data2, "%d/%m/%Y")

diferenca = abs((d2 - d1).days)

semanas = diferenca // 7
dias = diferenca % 7

if d1 > d2:
    maior = data1
elif d2 > d1:
    maior = data2
else:
    maior = "As datas são iguais"

print(f"\nDiferença em dias: {diferenca}")

print(f"Diferença: {semanas} semanas e {dias} dias")

print(f"Data maior: {maior}")

#questão 7

import re

texto = input("Digite o texto:\n")

emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    texto
)

telefones = re.findall(
    r'\(\d{2}\)\d{4,5}-\d{4}',
    texto
)

texto_limpo = re.sub(r'\s+', ' ', texto)

print("\nE-mails encontrados:")
for email in emails:
    print(email)

print("\nTelefones encontrados:")
for telefone in telefones:
    print(telefone)

print("\nTexto limpo:")
print(texto_limpo)