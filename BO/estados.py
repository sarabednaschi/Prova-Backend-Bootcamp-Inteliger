import core.models

class Estados():
    def lista_de_estados(self):
        dados = core.models.Estados.objects.order_by('id')
        return dados