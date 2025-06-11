from django.db import models

# Create your models here.
class About(models.Model):
    text = models.TextField()
    guarantees = models.TextField()

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
