from django.shortcuts import render
from django.views import generic
from .models import Court
# from django.views.generic import TemplateView

# views go below

# class HomePage(TemplateView):
#     """
#     Displays home page"
#     """
#     template_name = 'index.html'

class CourtList(generic.ListView):
    model = Court
    queryset = Court.objects.filter(status=1)
    template_name = "courts/index.html"
    paginate_by = 6