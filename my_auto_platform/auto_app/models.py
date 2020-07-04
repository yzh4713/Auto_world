from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    username=models.CharField(max_length=50)
    passworld=models.CharField(max_length=50)
    email=models.EmailField()
    createtime=models.DateTimeField()
    updatetime=models.DateTimeField(auto_now_add=True)
    upusername=models.CharField(max_length=50)
