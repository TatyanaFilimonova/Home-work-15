import datetime

import django
from django.db import models
from django.conf import settings
import django
from django.utils.translation import gettext_lazy as _

objects = models.Manager()

# Create your models here.

class Sports(models.Model):

    name = models.CharField(
        max_length=50)
    last_modified = models.DateTimeField(
        default=datetime.datetime.now()
    )

class Article(models.Model):

    name = models.ForeignKey(
        Sports,
        on_delete=models.CASCADE,
    )

    header = models.TextField(
    )

    short_text = models.TextField( null=False,
    )

    full_text = models.TextField(
    )

    tourney = models.CharField(
        max_length=50,
    )

    author = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    post_date = models.CharField(
        max_length=50)

    source = models.TextField()



