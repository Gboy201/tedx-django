from django.db import models

# Create your models here.

class sponsorRequests(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    organization = models.CharField(max_length=400)
    tier = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.organization

class teamMember(models.Model):
    full_name = models.CharField(max_length=100)
    pfp = models.ImageField(upload_to='images/')
    position = models.CharField(max_length=100, default="General")
    linkedin = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.full_name

class sponsorList(models.Model):
    tierChoices = [("Bronze", "Bronze"), ("Silver", "Silver"), ("Gold", "Gold"), ("Platinum", "Platinum")]
    organizationName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    tier = models.CharField(max_length = 100, choices=tierChoices)

    def __str__(self):
        return self.organizationName

class speaker(models.Model):
    full_name = models.CharField(max_length=100)
    pfp = models.ImageField(upload_to='images/')
    intro = models.TextField()

    def __str__(self):
        return self.full_name

    