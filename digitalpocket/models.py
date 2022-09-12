from django.db import models
from django.db.models.base import Model

# Create your models here.

class Fieldview(models.Model):
    field_id=models.AutoField(primary_key=True)
    field_name=models.CharField(max_length=30)
    field_image=models.ImageField(upload_to='fields/images',default="")
    field_select=models.CharField(max_length=30)
    def __str__(self):
        return (self.field_name)

class SubFieldView(models.Model):
    sub_field_id=models.AutoField(primary_key=True)
    sub_field_name=models.CharField(max_length=30)
    sub_field_image=models.ImageField(upload_to='fields/images/subImages',default="")
    sub_field_select=models.CharField(max_length=30)
    category_field=models.CharField(max_length=20)
    def __str__(self):
        return (self.sub_field_name)
class UploadedFile(models.Model):
    username=models.CharField(max_length=10,default='')
    category=models.CharField(max_length=30,default='')
    doc_title=models.CharField(max_length=300,default='')
    doc_image=models.FileField(upload_to='fields/images/uploaded',default="")

    def __str__(self):
        return (self.username)
