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
    date_register = models.DateField()
    
    def __unicode__(self):
        return self.name
    
class Funcionario(Dentista, models.Model):
    
    name = Dentista.name
    sex = Dentista.sexo
    date_entry = Dentista.date_register
    function = models.CharField(max_length=150, choices = FUNCTION)
    salary = models.FloatField()
    
    def __unicode__(self):
        return self.name

class CLiente(models.Model):

    name = models.CharField(max_length=150, unique=True)
    date_register = models.DateField()
    professional = models.ForeignKey(Dentista)
    time_contract = models.DateField()
    profession = models.CharField(max_length=150)
    type_plane = models.CharField(max_length = 150, choices = TYPE_PLANE)    
    
    def __unicode__(self):
        return self.name
