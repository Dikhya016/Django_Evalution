from django.db import models

# Create your models here.
class ServiceUser(models.Model):
    GENDER_CHOICE=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    age=models.IntegerField()
    gender=models.CharField(choices=GENDER_CHOICE,max_length=10)

    def __str__(self):
        return self.name

class Service(models.Model):
    SERVICE_TYPE=[
        ('Mobile Recharge','Mobile Recharge'),
        ('DTH Recharge','DTH Recharge'),
        ('Insurance payment','Insurance payment')
    ]
    PAYMENT_MODE=[
        ('UPI','UPI'),
        ('Internet banking','Internet banking'),
        ('Card payment','Card payment')
    ]
    typee=models.CharField( max_length=50,choices=SERVICE_TYPE)
    mode_of_payment=models.CharField(max_length=50,choices=PAYMENT_MODE)
    company=models.CharField(max_length=100)

    def __str__(self) :
        return self.company

class Subscriptions(models.Model):
    user=models.ManyToManyField(ServiceUser,related_name='user_subscription')
    service=models.ManyToManyField(Service, related_name='subscription')
    amount=models.IntegerField()
    current_date=models.DateField(auto_now=True)

