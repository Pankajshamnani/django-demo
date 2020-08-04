from django.db import models

class Shoe(models.Model):
    price=models.IntegerField()
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()