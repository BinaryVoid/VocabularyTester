from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.text import slugify

class vocabulary(models.Model):
	title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    