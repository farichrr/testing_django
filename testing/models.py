from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="Publisher name")
    website = models.URLField(help_text="Publisher's website address")
    email = models.EmailField(help_text="Publisher's email address")

    def __str__(self):
        return self.name