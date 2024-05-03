from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Food(TimeStampedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='foods/', null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    pass


class About(TimeStampedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='foods/', null=True, blank=True)
    location = models.CharField(max_length=212)

    def __str__(self):
        return self.name