from django.db import models

class Rating(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    score = models.IntegerField()

    def __str__(self):
        return self.name


# Create your models here.