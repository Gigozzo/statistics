from django.db import models

# Create your models here.

class Statistics(models.Model):
    dt = models.DateTimeField(primary_key=True)
    spam = models.IntegerField()
    notspam = models.IntegerField()
    reverts = models.IntegerField()
    complaints = models.IntegerField()
    total = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'statistics'
