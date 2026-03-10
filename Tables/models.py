from django.contrib.auth.models import User
from django.db import models


class DiningTable(models.Model):
    table_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.table_name
