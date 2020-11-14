# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Review, ContactForm


def index(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:3]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/index.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def reviews(request):
    review_list = Review.objects.order_by('-pub_date')
    context = {'review_list': review_list}
    return render(request, 'reviews/allReviews.html/', context)


def about(request):
    response = "You're looking at the about page"
    return HttpResponse(response)


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
