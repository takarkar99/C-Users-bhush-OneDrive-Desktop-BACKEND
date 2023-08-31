from django.db import models
from application_generation_app.models import Application


class Loan(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='Loans')
    loan_principal_amount = models.FloatField(default=0, blank=True)
    loan_tenure = models.FloatField(default=0, blank=True)
    interest_rate = models.FloatField(default=0, blank=True)
    total_amount_and_processing_fees = models.FloatField(default=0, blank=True)
    installment = models.IntegerField(default=0, blank=True)
    maturity_date = models.DateField(default="2000-12-12", blank=True)
    sanction_letter = models.FileField(upload_to='customer/loan/', default=0, blank=True)
    LOAN_STATUS_CHOICE = [
        ('Pending', 'Pending'),
        ('Sanctioned', 'Sanctioned'),
        ('Rejected', 'Rejected')
    ]
    status = models.CharField(max_length=250, choices=LOAN_STATUS_CHOICE, default=0, blank=True)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)

    def __str__(self):
        return f'{self.id}'


class Vendor(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='Vendors')
    name = models.CharField(max_length=250, default=0, blank=True)
    vendor_type = models.CharField(max_length=250, default=0, blank=True)
    email = models.EmailField(default=0, blank=True)
    address = models.TextField(max_length=250, default=0, blank=True)
    city = models.CharField(max_length=250, default=0,blank=True)
    state = models.CharField(max_length=250, default=0, blank=True)
    country = models.CharField(max_length=250, default=0, blank=True)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10,default=0, blank=True)
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    passbook_copy = models.FileField(upload_to='customer/vendor/', default=0, blank=True)
    current_account_no = models.CharField(max_length=25, default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)

    def __str__(self):
        return f"{self.id}"

