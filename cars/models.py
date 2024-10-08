from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50, blank = True,null = True)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    brand = models.ManyToManyField(Brand)
    #brand = models.ForeignKey(User, on_delete=models.CASCADE, blank = True,null = True)
    image = models.ImageField(upload_to='posts/media/uploads/', blank = True,null = True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username}'
    