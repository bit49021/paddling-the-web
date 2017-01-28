from django.db import models

# Create your models here.

class NewsArticle(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.title
