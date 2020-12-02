from django.db import models

# Create your models here.
class Scrapper(models.Model):
    resume_file=models.FileField(upload_to="files")