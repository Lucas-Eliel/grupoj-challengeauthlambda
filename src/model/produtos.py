class Produtos:

    def __init__(self, dados_recognizer):
        self.nome = ""
        self.quantidade = ""
        self.valor = ""
        self.dados_recognizer = dados_recognizer

    def to_dict(self):

        produtos = []

        if self.dados_recognizer.fields.get("Items") is not None:
            for item in self.dados_recognizer.fields.get("Items").value:
                self.nome = ""
                self.quantidade = ""
                self.valor = ""

                if item.value.get("Name") is not None:
                    self.nome = item.value.get("Name").value
                if item.value.get("Price") is not None:
                    self.valor = item.value.get("Price").value / 100

                produto = {
                    "nome": self.nome,
                    "quantidade": self.quantidade,
                    "valor": self.valor,
                }

                produtos.append(produto)

        return produtos