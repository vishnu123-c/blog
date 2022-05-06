from re import T
from django.db import models
from django.utils.text import slugify

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True,null=True)
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(post,self).save(*args,**kwargs)
