# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username

class Payment(models.Model):
    payer = models.ForeignKey(UserProfile, related_name='payments_made', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recipients = models.ManyToManyField(UserProfile, related_name='payments_received')
    split_equally = models.BooleanField(default=False)
    date_paid = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.payer.username} paid {self.amount} on {self.date_paid}"