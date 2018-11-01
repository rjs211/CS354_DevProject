from django.db import models

# Create your models here.
class Certif(models.Model):
    certifName = models.CharField(max_length=100)
    # certifSlug = models.SlugField()
    certifDesc = models.TextField()
    # add in author later

    def __str__(self):
        return self.certifName

    def snippet(self):
        return self.certifDesc[:50] + '...'
