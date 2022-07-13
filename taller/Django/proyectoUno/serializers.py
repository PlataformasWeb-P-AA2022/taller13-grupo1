from django.contrib.auth.models import User, Group
from proyectoUno.models import Departamento, Edificio

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        # fields = ['id', 'telefono', 'tipo']
        fields = '__all__' 
