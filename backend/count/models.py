from django.db import models

# Create your models here.
class Count(models.Model):
    title = models.CharField(max_length=200, default="count", null=True)
    number = models.IntegerField()

    def __str__(self):
        return self.title

class TotalCount(models.Model):
    title = models.CharField(max_length=200, default="total_count", null=True)
    numbers = models.ManyToManyField(Count, null=True)
    total = models.IntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        data = 0
        for number in self.numbers.all():
            data += number.number
        self.total = data
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.title