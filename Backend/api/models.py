from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 30)
    
    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length= 60)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    slug = models.SlugField(unique= True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='posts')
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"    
        