from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title


# Create your models here.
customer_type = (
    ("Active", "Active"),
    ("Inactive", "Inactive")
)


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=True)
    last_name = models.CharField(
        max_length=50, null=False, blank=True)
    other_names = models.CharField(max_length=50, default=" ")
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=30, null=False, blank=True)
    balance = models.IntegerField(default="0")
    customer_status = models.CharField(
        max_length=100, choices=customer_type, default="Active")
    address = models.CharField(
        max_length=50, null=False, blank=False)

    def save(self, *args, **kwargs):
        return super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return "{}:{}".format(self.first_name, self.last_name)
