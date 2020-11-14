from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:review_id>/', views.review_detail, name='review_detail'),

    path('allReviews/', views.reviews, name='allReviews'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact_view, name='contact'),

    path('success/', views.success_view, name='success')

]