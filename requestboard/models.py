from django.db import models

# Create your models here.

class SongRequest_Post(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=15, default='Author')
    content = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'[{self.pk}] {self.title}'
    

    def get_absolute_url(self):
        return f'/requestboard/{self.pk}'
