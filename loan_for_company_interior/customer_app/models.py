from django.db import models


class Enquiry(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    message = models.TextField()
    enquiry_date = models.DateTimeField(auto_now_add=True, blank=True)
    ENQUIRY_STATUS = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=50, default='', choices=ENQUIRY_STATUS)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.id}"
