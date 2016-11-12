from __future__ import unicode_literals

from django.db import models
from app_clinica.models import *

TYPE_PRODUCT = ((u'Limpeza','Limpeza'),(u'Escritorio','Escritorio')
,(u'Informatica','Informatica'),(u'Bucal profissional','Bucal profissional'),(u'Bucal venda','Bucal venda'))

class Base(models.Model):
    name = models.CharField(max_length = 150)
    amount_float = models.FloatField()
    amount_int = models.IntegerField()
    date = models.DateField()
    date_timed = models.DateTimeField()
    choice = models.CharField(max_length = 150)
            
class Produto(Base, models.Model):
    
    name = Base.name
    amount = Base.amount_int
    value_per_unit_to_buy = Base.amount_float
    purchase_date = Base.date
    date_vaidate = Base.date
    product_type = Base.choice.choices=TYPE_PRODUCT
    
    def __unicode__(self):
        return self.name
        
class Retira_Produto(Base,models.Model):

    product = models.ForeignKey(Produto)
    date_for_withdrawal = Base.date_timed
    amount_withdrawal = Base.amount_float
    responsible = models.ForeignKey(Funcionario)
    amout_refresh = models.CharField(max_length=150)# Sera atualizada pelo formulario

    def __unicode__(self):
        return self.product