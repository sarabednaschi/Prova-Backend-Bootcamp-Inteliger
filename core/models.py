from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(null=True, max_length=200)
    sexo = models.CharField(null=True, max_length=200)
    data_nascimento = models.DateField(null=True)

    class Meta:
        db_table = 'pessoas'


class Estados(models.Model):
   nomes =  models.CharField(null=True, max_length=200)
   siglas = models.CharField(null=True, max_length=200)

   class Meta:
        db_table = 'estados'