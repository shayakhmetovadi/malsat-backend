from django.db import models
from django.contrib.auth import get_user_model  # 1 var
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager  # 2 var
import time
from django.core.validators import RegexValidator
from django.db.models import Q

User = get_user_model()



def upload_file(instance, filename):
    lastDot = filename.rfind('.')  # поиск с конца точку
    extension = filename[lastDot:len(filename):1]
    return 'media/file/%s-%s%s' % (instance.name, time.time(), extension)


class Region(models.Model):
    regionName = models.CharField(max_length=255, blank=True, null=True)


class Category(models.Model):
    categoryName = models.CharField(max_length=255, blank=True, null=True)


class Subcategory(models.Model):
    subcategoryName = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


class Item(models.Model):
    itemName = models.CharField(max_length=255, blank=True, null=True)
    itemDescription = models.TextField(blank=True, null=True)
    itemPrice = models.DecimalField(decimal_places=1, max_digits=900, blank=True, null=True)
    images = models.FileField(upload_to="images", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    itemCreated = models.DateTimeField(auto_now_add=True, blank=True)
    itemExchange = models.BooleanField(default=False)


class Comment(models.Model):
    commentText = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    commentDate = models.DateTimeField(auto_now_add=True, blank=True)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)