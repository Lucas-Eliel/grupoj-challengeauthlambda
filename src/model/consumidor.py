class Consumidor:

    def __init__(self, dados_recognizer):
        self.cpf = ""
        self.nome = ""
        self.dados_recognizer = dados_recognizer

    def to_dict(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
        }