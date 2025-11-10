from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.name

from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length =  50, unique = True)

    def __str__(self):
        return self.name

#in terminal

python manage.py makemigrations home
python manage.py migrate