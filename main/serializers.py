from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Portfolio,Details


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['name','phone','email']
