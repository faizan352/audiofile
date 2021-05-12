from django.db import models

# Create your models here.

class song(models.Model):

    def __str__(self):
        return self.s_name

    s_name = models.CharField(max_length=100)
    s_duation = models.DurationField()
    s_uploaded_time = models.TimeField()

class podcast(models.Model):

    def __str__(self):
        return self.p_name
    
    p_name = models.CharField(max_length=100)
    p_duation = models.DurationField()
    p_uploaded_time = models.TimeField()
    p_host = models.CharField(max_length=100)
    p_participants = models.CharField(max_length=100)

class audiobook(models.Model):

    def __str__(self):
        return self.a_title

    a_title = models.CharField(max_length=100)
    a_author = models.CharField(max_length=100)
    a_narrator = models.CharField(max_length=100)
    a_duration = models.DurationField()
    a_uploaded_time =models.TimeField()