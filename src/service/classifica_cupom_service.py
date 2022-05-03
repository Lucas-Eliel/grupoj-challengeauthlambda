from src.model.enum.Status import Status


class ClassificaCupomService:

    def __init__(self, cupom):
        self.cupom = cupom

    def classificar(self):
        self.cupom['status_cupom'] = self.definir_status()
        self.cupom['ranking'] = self.definir_ranking()

    def definir_ranking(self):
        ranking = 100

        #Estabelecimento vale 15%
        if self.cupom['estabelecimento']['cnpj'] == "":
            ranking -= 5
        if self.cupom['estabelecimento']['nome'] == "":
            ranking -= 5
        if self.cupom['estabelecimento']['endereco'] == "":
            ranking -= 5

        # Consumidor vale 10%
        if self.cupom['consumidor']['cpf'] == "":
            ranking -= 5
        if self.cupom['consumidor']['nome'] == "":
            ranking -= 5

        # Produto vale 50%
        for produto in self.cupom['produtos']:
            if produto['nome'] == "":
                ranking -= 10
            if produto['quantidade'] == "":
                ranking -= 10
            if produto['valor'] == "":
                ranking -= 30

        # Total vale 25%
        if self.cupom['valor_total'] == "":
            ranking -= 25

        return ranking

    def definir_status(self):
        if self.is_total_igual_soma_itens() and self.is_estabelecimento_possui_cnpj() and self.is_produto_possui_descricao():
            return Status.VALIDO.value
        return Status.INVALIDO.value

    # 1 - soma dos produtos ser igual ao valor total 70%
    def is_total_igual_soma_itens(self):
        if self.cupom['valor_total'] == "":
            return False

        for produto in self.cupom['produtos']:
            if produto['valor'] == "" or produto['valor'] is None:
                return False

        soma_itens = 0

        for produto in self.cupom['produtos']:
            soma_itens += produto['valor']

        if not self.cupom['valor_total'] == soma_itens:
            return False

        return True

    # 2 - ler cnpj -> estabelecimento 15%
    def is_estabelecimento_possui_cnpj(self):
        if self.cupom['estabelecimento']['cnpj'] == "":
            return False
        return True

    # 3 - produto -> descricao 15%
    def is_produto_possui_descricao(self):
        for produto in self.cupom['produtos']:
            if produto['nome'] == "":
                return False
        return True