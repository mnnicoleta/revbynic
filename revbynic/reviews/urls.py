from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),

    path('allReviews/', views.reviews, name='allReviews'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact')

]