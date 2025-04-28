from djongo import models  # Correct for Djongo

class Product(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
