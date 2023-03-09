from django.db import models


class ContactBase(models.Model):
    """
    Email subscriber

    """
    name = models.CharField(max_length=36)
    email = models.EmailField(max_length=36)

    def __str__(self):
        return self.name
