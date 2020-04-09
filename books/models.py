from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    num_pages = models.IntegerField(max_length=100)
    date_published = models.DateField(blank=True, Null=True)

    def __str__(self):
        return self.title