from django.urls import path
from .views import SendMailView


urlpatterns = [
    path('mail/<int:pk>/', SendMailView.as_view(), name='mail')
]