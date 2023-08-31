from rest_framework import viewsets
from .models import Application, Guarantor, Document
from .Serializers import ApplicationSerializer, GuarantorSerializer, DocumentSerializer
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import Application
from rest_framework.views import APIView
from admin_app.models import User


class ApplicationVIew(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class GuarantorView(viewsets.ModelViewSet):
    serializer_class = GuarantorSerializer
    queryset = Guarantor.objects.all()


class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Guarantor.objects.all()


class SendMailView(APIView):
    
    def post(self, request, pk):
        obj = User.objects.get(pk = pk)
        print(obj.email)
        return Response(
        send_mail(
            'Application Generated',
            f"your loan application is generated. application Id is {pk}",
            'bhushantakarkar99@gmail.com',
            [obj.email],
            fail_silently=False,)
        )