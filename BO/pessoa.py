import core.models

class Pessoa():
    def lista_de_pessoas(self):
        dados = core.models.Pessoa.objects.filter(sexo='F').order_by('id')
        return dados
