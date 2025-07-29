from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    customer_since = models.DateField(null=False)

    def __str__(self):
        return self.customer_name