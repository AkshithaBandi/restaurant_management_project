from django.db import models

# Create your models here.
status = models.ForeignKey(OrderStatus,on_delete = models.SET_NULL, null = True)

class Coupon(models.Model):
    code = models.CharField(max_length = 50, unique = True)
    discount_percentage = models.DecimalField(max_digits = 5, decimal_places = 2)
    is_active = models.BooleanField
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code
        
#in terminal
python manage.py makemigrations orders
python manage.py migrate