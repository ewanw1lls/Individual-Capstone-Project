from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Court
# from django.views.generic import TemplateView

# class based views go below

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

# function based views go below
 
def court_detail(request, slug):
    """
    Display an individual :model:`courts.court`.

    **Context**

    ``court``
        An instance of :model:`courts.court`.

    **Template:**

    :template:`courts/court_detail.html`
    """

    queryset = Court.objects.filter(status=1)
    court = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "courts/court_detail.html",
        {"court": court},
    )