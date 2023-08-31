from rest_framework import serializers
from .models import User, Family, Bank


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class FamilySerializers(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'