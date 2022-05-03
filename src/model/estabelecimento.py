class Estabelecimento:

    def __init__(self, dados_recognizer, cnpj):
        self.cnpj = cnpj
        self.nome = ""
        self.endereco = ""
        self.dados_recognizer = dados_recognizer

    def to_dict(self):

        if self.dados_recognizer.fields.get("MerchantAddress") is not None:
            self.endereco = self.dados_recognizer.fields.get("MerchantAddress").value

        if self.dados_recognizer.fields.get("MerchantName") is not None:
            self.nome = self.dados_recognizer.fields.get("MerchantName").value

        return {
            "cnpj": self.cnpj,
            "nome": self.nome,
            "endereco": self.endereco,
        }