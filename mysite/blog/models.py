from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ContactBlog(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name
