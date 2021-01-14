from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    cv_file = models.FileField(upload_to='document')
    
    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='portfolio')
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length = 100)
    description = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.job_title



 
   
