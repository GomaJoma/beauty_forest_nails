from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Published Date', auto_now_add=True)

    def __str__(self):
        return str(self.pub_date)
