from django.shortcuts import render
from django.views import generic
from .models import Court
# from django.views.generic import TemplateView

#views go below

# class HomePage(TemplateView):
#     """
#     Displays home page"
#     """
#     template_name = 'index.html'

class CourtList(generic.ListView):
    model = Court
    template_name = "courts/court_list.html"