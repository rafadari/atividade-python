from jogo.dados import lancar_dado
from jogo.eventos import SistemaEventos

sistema = SistemaEventos()

def sorte():
    print("Você tirou 6! Evento de sorte ativado!")

def azar():
    print("Você tirou 1! Evento de azar ativado!")

sistema.registrar(6, sorte)
sistema.registrar(1, azar)

resultado = lancar_dado()

print(f"Resultado do dado: {resultado}")

sistema.disparar(resultado)