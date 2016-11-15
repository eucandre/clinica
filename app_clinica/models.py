from __future__ import unicode_literals

from django.db import models

PAYMENT_MODEL=((u'CCredito','CCredito'),(u'CDebito', 'CDebito'),
               (u'Boleto', 'Boleto'), (u'Dinheiro', 'Dinheiro'),
                (u'Cheque','Cheque'))

TYPE_PLANE = ((u'Plano', 'Plano'), (u'Avulso','Avulso'))

FUNCTION = ((u'Gerente','Gerente'),(u'Zelador(a)','Zelador(a)'),
            (u'Atendente', 'Atendente'), (u'Vigia','Vigia'),
            (u'Seguranca', 'Seguranca'))

SEXO = ((u'Masculino','Masculino'),(u'Feminino','Feminino'))


class Dentista(models.Model):

    name = models.CharField(max_length=150, unique = True)
    sex = models.CharField(max_length=150, choices=SEXO)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    active = models.BooleanField()


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dentistas"

class Funcionario(Dentista, models.Model):

    name = Dentista.name
    date_entry = models.DateField()
    sex = Dentista.sex
    function = models.CharField(max_length=150, choices = FUNCTION)
    email = Dentista.email
    phone = Dentista.phone
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    salary = models.FloatField()
    active = Dentista.active

    def __unicode__(self):
        return self.name


class Cliente(models.Model):

    name = models.CharField(max_length=150, unique = True)
    date_register = models.DateField()
    professional = models.ForeignKey(Dentista)
    time_contract = models.DateField()
    type_plane = models.CharField(max_length = 150, choices = TYPE_PLANE)
    profession = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    active = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Clientes'