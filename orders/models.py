from django.db import models

# Create your models here.
status = models.ForeignKey(OrderStatus,on_delete = models.SET_NULL, null = True)

#in terminal
python manage.py makemigrations orders
python manage.py migrate