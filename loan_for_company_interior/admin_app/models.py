from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    GENDER_CHOICES = [('male','male'),('female','female')]

    last_name = models.CharField(max_length=250)
    dob = models.DateField(default="2000-12-12", blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.IntegerField()
    photo = models.FileField(upload_to="customer/user/", default=0, blank=True)
    signature = models.FileField(upload_to="customer/user/", default=0, blank=True)
    

    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']


class Family(models.Model):

    MARITAL_STATUS =[('married','married'),('unmarried','unmarried')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Familys')
    father_name = models.CharField(max_length=250, default=0, blank=True)
    father_profession = models.CharField(max_length=250, default=0, blank=True)
    mother_name = models.CharField(max_length=250, default=0, blank=True)
    mother_profession = models.CharField(max_length=250, default=0, blank=True)
    marital_status = models.CharField(max_length=250, choices=MARITAL_STATUS, default=0, blank=True)
    spouse_name = models.CharField(max_length=250, default=0, blank=True)
    spouse_profession = models.CharField(max_length=250, default=0, blank=True)
    mobile = models.IntegerField(default=0, blank=True)
    address = models.TextField(default=0, blank=True)

    def __str__(self):
        return f'{self.id}'


class Bank(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Banks')
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    current_account_no = models.CharField(max_length=20, default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)
    passbook_copy = models.FileField(upload_to='media/customer/bank/', default=0, blank=True)

    def __str__(self):
        return f'{self.id}'