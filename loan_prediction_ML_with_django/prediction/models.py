from django.db import models

class file_upload(models.Model):
    file = models.FileField()
