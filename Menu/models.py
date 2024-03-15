from django.db import models

# class Banner(models.Model):
#     title = models.CharField(max_length=255)
#     body = models.TextField()

#     def __str__(self):
#         return self.title
    

class AboutUs(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body
    

class Service(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='service/')
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Blog(models.Model):
    title = models.CharField(max_length = 255)
    body  = models.TextField()
    image = models.FileField(upload_to='blog/')

