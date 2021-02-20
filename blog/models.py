from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000, null=False, blank=False)
    image = models.ImageField(upload_to="images/")
    createdDate = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique_with='createdDate__month', null=False)
    # slug = models.SlugField(max_length = 250, null = True, blank = True)
    description = models.TextField()
    published = models.BooleanField(default=False)
    lastUpdated = models.DateTimeField(blank=True, null=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self): 
        return self.title

class blogUser(models.Model):
    first_name = models.CharField(max_length=100, blank=False,null=False)
    email = models.EmailField(max_length=150, blank=False,null=False)
    password = models.CharField(max_length=50, blank=False,null=False)
    username = models.CharField(max_length=100, blank=False,null=False)

    # object = UserManager()
    class Meta:
        '''docstring for meta'''
        verbose_name_plural = "User"