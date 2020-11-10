import os
from datetime import datetime, timedelta, timezone
from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.timezone import now


class Review(models.Model):
    rev_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.rev_text + str(self.pub_date)

    def was_published_recently(self):
        return datetime.now() - timedelta(days=1) <= self.pub_date <= datetime.now()


class Document(models.Model):
    document = models.FileField(upload_to=os.path.abspath('reviews/uploads/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)
    review_fk = models.ForeignKey(Review, on_delete=models.CASCADE)
