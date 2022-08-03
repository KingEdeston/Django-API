from csv import field_size_limit
from rest_framework import serializers
from .models import CertForm, Item, StudentData

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields ='__all__'


class CertFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['wid', 'lastName']

class DataFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = '__all__'





"""
class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('text')
"""