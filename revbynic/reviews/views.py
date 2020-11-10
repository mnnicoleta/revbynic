# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Review, Document


class IndexView(generic.ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'latest_review_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Review.objects.order_by('-pub_date')[:3]


class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'


def reviews(request):
    review_list = Review.objects.order_by('-pub_date')
    document_list = Document.objects
    context = {'review_list': review_list, 'document_list': document_list}
    return render(request, 'reviews/reviews.html', context)


def about(request):
    response = "You're looking at the about page"
    return HttpResponse(response)


def contact(request):
    response = "You're looking at the contact page"
    return HttpResponse(response)
