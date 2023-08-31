from django.shortcuts import render


from rest_framework import viewsets
from .Serializers import UserSerializers, FamilySerializers, BankSerializers
from .models import User, Family, Bank


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class FamilyView(viewsets.ModelViewSet):
    serializer_class = FamilySerializers
    queryset = Family.objects.all()


class Bankview(viewsets.ModelViewSet):
    serializer_class = BankSerializers
    queryset = Bank.objects.all()