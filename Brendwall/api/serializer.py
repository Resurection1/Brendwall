from rest_framework import serializers

from api.models import TestModels


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModels
        fields = ['title', 'description', 'price']
