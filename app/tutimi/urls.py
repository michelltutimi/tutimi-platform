from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, {'lang': 'en'}, name='home_en'),
    path('es/', views.home, {'lang': 'es'}, name='home_es'),
    path('case-studies', views.case_studies, name='case_studies'),
]