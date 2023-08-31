from rest_framework import viewsets
from .models import Enquiry
from .Serializers import EnquirySerializers
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
import logging




class EnquiryViewSet(viewsets.ModelViewSet):
    serializer_class = EnquirySerializers
    queryset = Enquiry.objects.all()
    
    logger = logging.getLogger('django')

    def create(self, request, *args, **kwargs,):
        resp = super().create(request, *args, **kwargs)
        first_name = resp.data.get('first_name')
        email = resp.data.get('email')
        enq_id = resp.data.get('id')
        subject = "Mail about Loan Enquiry"
        message = f"Hello {first_name}\nThank you for contacting us about loan.\nPlease Visit the link to check the status of your enquiry\n"\
            f'http://localhost:8000/api/enquiry/{enq_id}/check_status/\n\n'\
           "Check Status :\n" f'http://localhost:3000/getstatus/{enq_id}/'    
            
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message,email_from, [email,])
        self.logger.info('user created successfully')
        self.logger.error('This is Errro for Mail.')
        return resp
    
    @action(detail=True, methods=['GET'])
    def check_status(self,request,pk=None):
        obj = self.get_object()
        if obj.status == 'Approved':
            data = {'detail':"Your Enquiry is Succefully Completed"}
            return Response(data=data, status=200)
        return Response(data={'detail':'Your Enquiry is still in process , Please Check back later. '})
    


    