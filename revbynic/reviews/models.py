import os
from datetime import timezone, datetime
from django.db import models


# Create your models here.

class Review(models.Model):
    rev_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.rev_text + str(self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Document(models.Model):
    document = models.FileField(upload_to=os.path.abspath('reviews/uploads/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)
    review_fk = models.ForeignKey(Review, on_delete=models.CASCADE)

