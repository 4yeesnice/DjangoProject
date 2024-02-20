from django.db import models

# Create your models here.

class Blogs( models.Model ):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title + " Description: " + self.description[:20]