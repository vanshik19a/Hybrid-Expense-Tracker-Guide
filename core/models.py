from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, blank=True, default="")

    def __str__(self):
        return f"{self.description} - ₹{self.amount}"
