from datetime import datetime

from django.db import models

# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(default=datetime.now, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'tweets'
        verbose_name = 'tweet'
        ordering = ("-creation_date",)

    def __str__(self):
        return self.content

