# Create your views here.
from django import template
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Review, ContactForm, Document


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


def last_documents(request):
    all_doc_list = Document.objects.order_by('-uploaded_at')[:3]
    context = {'all_doc_list': all_doc_list}
    return render(request, 'reviews/allDocuments.html/', context)


def documents(request):
    all_doc_list = Document.objects.order_by('-uploaded_at')
    for doc in all_doc_list:
        doc.document.name = cut(doc.document.name, 'C:/Users/nicoleta.manea/PycharmProjects/revbynic/revbynic/reviews/static')
    context = {'all_doc_list': all_doc_list}
    return render(request, 'reviews/allDocuments.html/', context)


def about(request):
    return render(request, 'reviews/about.html')


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
            return redirect('/reviews/success/')
    return render(request, "reviews/contact.html", {'form': form})


def success_view(request):
    return render(request, 'reviews/success.html')


register = template.Library()


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

