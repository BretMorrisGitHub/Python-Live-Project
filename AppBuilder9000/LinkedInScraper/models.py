from django.db import models

# Create user model

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=15)
    email_addr = models.CharField(max_length=30)
    linkedin_id = models.CharField(max_length=100)
    company = models.CharField(max_length=30)

    # defines the model manager for users
    Users = models.Manager()


