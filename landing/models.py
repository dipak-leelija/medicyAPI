from django.db import models

# Own models here.
# class Plans(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=55)
#     price = models.FloatField()
#     duration = models.CharField(max_length=20)
#     status = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'plans'

class PlansFeatures(models.Model):
    plan_id  = models.IntegerField(primary_key = True)
    features = models.CharField(max_length = 100)
    status   = models.IntegerField() 

    class Meta:
        managed =False
        db_table = 'plans_features'
