from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    status = models.IntegerField()

    class Meta:
        db_table = 'plans'
