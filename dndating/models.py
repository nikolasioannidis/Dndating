from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class category_edition(models.Model):
    category_edition = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.category_edition}"

class category_Class(models.Model):
    category_Class = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.category_Class}"

class category_gender(models.Model):
    category_gender = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.category_gender}"

class info(models.Model):
    edition= models.ForeignKey(category_edition, on_delete=models.CASCADE, blank=True, null=True, related_name="edition")
    Class= models.ForeignKey(category_Class, on_delete=models.CASCADE, blank=True, null=True, related_name="Class")
    discription = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="USER")
    IsActive = models.BooleanField(default=True)
    discord = models.CharField(null=True, max_length=50)
    facebook = models.CharField(null=True, max_length=50)
    instagram = models.CharField(null=True, max_length=50)
    genter =  models.ForeignKey(category_gender, on_delete=models.CASCADE, blank=True, null=True, related_name="gender")
    years_playing = models.CharField(null=True, max_length=50)

    def __str__(self):
        return f"{self.name}"


class FilesUpload(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name}"