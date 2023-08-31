from django.db import models
from admin_app.models import User


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Applications')
    aadhaar_no = models.CharField(max_length=12, default=0, blank=True)
    pan_no = models.CharField(max_length=10, default=0, blank=True)
    EMPLOYMENT_CHOICE = [
        ('Self_Employed', 'Self_Employed'),
        ('Regular_Salaried', 'Regular_Salaried')
    ]
    type_of_employment = models.CharField(max_length=250, choices=EMPLOYMENT_CHOICE, default=0, blank=True)
    business_title = models.CharField(max_length=250, default=0, blank=True)
    BUSINESS_TYPE = [
        ('Services', 'Services'),
        ('Manufacturing', 'Manufacturing'),
        ('Wholesaling', 'Wholesaling'),
        ('Retailing', 'Retailing'),
        ('Other', 'Other')
    ]
    business_type = models.CharField(max_length=250, choices=BUSINESS_TYPE, default=0, blank=True)
    business_address = models.TextField(default=0, blank=True)
    gst_registration_no = models.CharField(max_length=50, default=0, blank=True)
    business_license_no = models.CharField(max_length=50, default=0, blank=True)
    expected_average_annual_turnover = models.CharField(max_length=250, default=0, blank=True)
    years_in_current_business = models.IntegerField(default=0, blank=True)
    collateral = models.CharField(max_length=250, default=0, blank=True)
    APPLICATION_STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')

    ]
    status = models.CharField(max_length=250, default='', choices=APPLICATION_STATUS)
    application_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)

    def __str__(self):
        return f"{self.id}"
    

class Guarantor(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='Guarantors')
    relation_with_customer = models.CharField(max_length=250, default=0, blank=True)
    name = models.CharField(max_length=150, default=0, blank=True)
    dob = models.DateField(default="2000-12-12", blank=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
        ]
    gender = models.CharField(max_length=50,  default=0, blank=True, choices=GENDER_CHOICES)
    email = models.EmailField(default=0, blank=True)
    address = models.TextField(max_length=250, default=0, blank=True)
    city = models.CharField(max_length=50, default=0,blank=True)
    state = models.CharField(max_length=50, default=0,blank=True)
    country = models.CharField(max_length=250, default=0, blank=True)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10,default=0, blank=True)
    photo = models.ImageField(upload_to='media/customer/guarantor/', default=0, blank=True)
    profession = models.CharField(max_length=250, default=0, blank=True)
    income_certificate = models.FileField(upload_to='media/customer/guarantor/', default=0, blank=True)
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    current_account_no = models.CharField(max_length=20, default=0, blank=True)
    passbook_copy = models.FileField(upload_to='media/customer/guarantor/', default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)

    def __str__(self):
       	return f'{self.id}'
    

class Document(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='Documents')
    aadhaar_card = models.FileField(upload_to='customer/document/', default=0, blank=True)
    pan_card = models.FileField(upload_to='customer/document/', default=0, blank=True)
    business_address_proof_or_copy_of_rent_agreement = models.FileField(upload_to='customer/document/', default=0, blank=True)
    electricity_bill = models.FileField(upload_to='customer/document/', default=0, blank=True)
    msme_certificate = models.FileField(upload_to='customer/document/', default=0, blank=True)
    gst_certificate = models.FileField(upload_to='customer/document/', default=0, blank=True)
    udyog_aadhaar_registration = models.FileField(upload_to='customer/document/', default=0, blank=True)
    business_license = models.FileField(upload_to='customer/document/', default=0, blank=True)
    business_plan_or_proposal = models.FileField(upload_to='customer/document/', default=0, blank=True)
    three_year_itr_with_balance_sheet = models.FileField(upload_to='customer/document/', default=0, blank=True)
    collateral_document = models.FileField(upload_to='customer/document/', default=0, blank=True)
    stamp_duty = models.FileField(upload_to='customer/document/', default=0, blank=True)
    DOCUMENT_STATUS_CHOICE = [
        ('Processed', 'Processed'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
        ]
    status = models.CharField(max_length=250, choices=DOCUMENT_STATUS_CHOICE, default=0, blank=True)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)

    def __str__(self):
       	return f'{self.id}'


