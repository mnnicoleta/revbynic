import os
from datetime import datetime, timedelta
from django.db import models
from django import forms
# Create your models here.


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


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)