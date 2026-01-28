from django.db import models

# Create your models here.
class Leaves(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    cno=models.IntegerField()
    msg=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='image/', default='/image/')

    class Meta:
        db_table = 'Leaves'