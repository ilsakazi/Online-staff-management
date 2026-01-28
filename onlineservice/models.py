from django.contrib.auth.models import User
from django.db import models

from .util import *
# Create your models here.
class Register(models.Model):
    user=models.OneToOneField(User,models.CASCADE)
    address=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='img/', default='/img/')

    def __str__(self):
        return self.user.username
class Faculty(models.Model):
    user=models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to='image/', default='/image/')
    roomno=models.CharField(max_length=50)
    div=models.CharField(max_length=50)
    sem=models.TextField(blank=True, null=True)
    subject=models.CharField(max_length=50)

    class Meta:
        db_table='Faculty'

    def save(self, *args, **kwargs):
        self.slug = generateslug(self.name)
        super(Faculty, self).save(*args, **kwargs)
