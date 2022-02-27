from django.urls import path
from . import views

app_name = 'builder'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('cv/', views.download, name='download')
]
