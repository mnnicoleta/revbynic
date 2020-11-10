from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from datetime import datetime, timedelta

from .models import Review


class ReviewModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = datetime.now() + timedelta(days=30)
        future_review = Review(pub_date=time)
        self.assertIs(future_review.was_published_recently(), False)
