from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.last_documents, name='index'),

    path('<int:review_id>/', views.review_detail, name='review_detail'),

    path('allDocuments/', views.documents, name='allDocuments'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact_view, name='contact'),

    path('success/', views.success_view, name='success')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)