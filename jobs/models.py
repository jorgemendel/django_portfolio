from django.db import models

class Job(models.Model):
    # Images
    images = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)
    name = models.CharField(max_length=50, default="Project")

    def __str__(self):
        return self.summary
