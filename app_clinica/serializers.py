from rest_framework import serializers
from .models import *


class DentistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentista
        fields = ('name', 'sex', 'email', 'phone', 'active')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('name','date_register','professional','time_contract','profession','type_plane','email','phone','street','district','city','active')


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('name', 'sex', 'function','date_entry','email','phone','street','district','city','salary','active')