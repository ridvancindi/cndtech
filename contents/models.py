from unicodedata import name
from venv import create
from django.db import models
from taggit.managers import *
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class Category(models.Model):
    cat_name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.cat_name
class Lang(models.Model):
    name = models.CharField(max_length=20)
    lang_code = models.CharField(max_length=3,unique=True)
    def __str__(self):
        return self.name
class Maincontent(models.Model):
    auth = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,to_field="cat_name", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    url = models.CharField(max_length=75)
    summary = models.TextField(max_length=200)
    publication_date = models.DateField()
    situation =models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    upgrate_date = models.DateField(auto_now=True)
    cont_img = models.FileField(blank = True,upload_to= 'static/images')
    content = RichTextField()
    tags = TaggableManager()
    lang = models.ForeignKey(Lang, to_field="lang_code", on_delete=models.CASCADE)
    meta_titile = models.CharField(max_length=50)
    meta_content = models.CharField(max_length=100)
    meta_tag = models.CharField(max_length=50)
    def __str__(self):
        return self.title