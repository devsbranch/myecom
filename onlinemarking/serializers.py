from rest_framework import serializers
from .models import Iteam, Category


class IteamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Iteam
        fields = [
            'id',
            'name',
            'amount',
            'category'
        ]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'quantity'
        ]
