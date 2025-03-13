from . import views
from django.urls import path

urlpatterns = [
    path('', views.CourtList.as_view(), name='home'),
    path('<slug:slug>/', views.court_detail, name='court_detail'),
]
