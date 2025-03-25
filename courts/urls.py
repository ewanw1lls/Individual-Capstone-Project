from . import views
from django.urls import path


urlpatterns = [
    path('', views.CourtList.as_view(), name='home'),
    path('add-court/', views.add_court, name='add_court'),
    path('<slug:slug>/', views.court_detail, name='court_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
    path('court/<slug:slug>/<int:court_id>/edit/',
         views.court_edit, name='court_edit'),
    path('delete_court/<slug:slug>/<int:court_id>/',
         views.court_delete, name='court_delete'),
]
