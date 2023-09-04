from datetime import datetime
from django.db import models


class Memo(models.Model):
    idx = models.AutoField(primary_key=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    memo = models.CharField(max_length=2000, blank=True, null=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
