from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    '''日志'''
    title = models.CharField(verbose_name='标题', max_length=150, blank=False, null=False)
    content = RichTextField('正文') # 使用ckeditor中的RichTextFi

class Employee(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # image = models.CharField(max_length=50)

class upload(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)


def __unicode__(self):
    return self.name


# Create your models here.
