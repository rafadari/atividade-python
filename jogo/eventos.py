class SistemaEventos:

    def __init__(self):
        self.eventos = {}

    # registra um evento para um resultado
    def registrar(self, resultado, funcao):

        if resultado not in self.eventos:
            self.eventos[resultado] = []

        self.eventos[resultado].append(funcao)

    # dispara os eventos do resultado
    def disparar(self, resultado):

        if resultado in self.eventos:

            for funcao in self.eventos[resultado]:
                funcao()