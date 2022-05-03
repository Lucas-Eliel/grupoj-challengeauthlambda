import uuid

from src.model.consumidor import Consumidor
from src.model.estabelecimento import Estabelecimento
from src.model.produtos import Produtos


class Cupom:

    def __init__(self, dados_usuario):
        self.name = dados_usuario
        self.middle_name = ""
        self.email = ""
        self.locale = ""
        self.phone_number = ""
        self.address = ""

    def to_dict(self):

        return {
            "id_processo": self.id_processo,
            "status_cupom": self.status_cupom,
            "ranking": self.ranking,
            "estabelecimento": self.estabelecimento.to_dict(),
            "consumidor": self.consumidor.to_dict(),
            "produtos": self.produtos.to_dict(),
            "valor_total": self.valor_total
        }

