from app_form_html import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.user, name='users'),
]


