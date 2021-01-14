from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    cv_file = models.FileField(upload_to='document')
    
    def __str__(self):
        return self.title


