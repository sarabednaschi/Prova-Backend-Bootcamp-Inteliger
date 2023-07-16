from django.shortcuts import render
from django.views import View
import random
import BO.pessoa
import BO.estados


class ProvaPythonView(View):
    def get(self, *args, **kwargs):
        contexto = {}
        LISTA_NUMEROS_ALEATORIOS = [1,2,3,4,5,6,7,8,9,1] *10

        random.shuffle(LISTA_NUMEROS_ALEATORIOS)

        contexto['LISTA_NUMEROS_ALEATORIOS'] = LISTA_NUMEROS_ALEATORIOS

        soma = 0

        for numero in LISTA_NUMEROS_ALEATORIOS:
            soma = soma + numero

        contexto['soma'] = soma

        numeros_em_ordem_crescente = sorted(set(LISTA_NUMEROS_ALEATORIOS))

        contexto['numeros_em_ordem_crescente'] = numeros_em_ordem_crescente

        numeros_em_ordem_decrescente = sorted(set(LISTA_NUMEROS_ALEATORIOS), reverse=True)

        contexto['numeros_em_ordem_decrescente'] = numeros_em_ordem_decrescente

        lista_pessoas = [
            {'nome': 'Maria', 'idade': 20},
            {'nome': 'João', 'idade': 5},
            {'nome': 'Jose', 'idade': 60},
            {'nome': 'Bruna', 'idade': 20},
            {'nome': 'Lara', 'idade': 10},
        ]
        lista_pessoas_menor_de_idade = []

        for pessoa in lista_pessoas:
            if pessoa['idade'] < 18:
                lista_pessoas_menor_de_idade.append(pessoa)

        contexto['lista_pessoas_menor_de_idade'] = lista_pessoas_menor_de_idade

        return render(self.request, template_name='core/index.html', context=contexto)


class PessoaView(View):
    def get(self, *args, **kwargs):
        contexto = {}
        contexto['pessoas'] = []

        contexto['pessoas'] = BO.pessoa.Pessoa().lista_de_pessoas()

        contexto['titulo'] = 'Lista de pessoas'
        return render(self.request, template_name='core/pessoas.html', context=contexto)


class EstadoView(View):
    def get(self, *args, **kwargs):
        contexto = {}
        contexto['estados'] = []

        contexto['estados'] = BO.estados.Estados().lista_de_estados()

        contexto['titulo'] = 'Lista de estados'
        return render(self.request, template_name='core/estados.html', context=contexto)


