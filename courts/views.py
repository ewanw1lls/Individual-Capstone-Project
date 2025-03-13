from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Court
from .forms import ReviewForm
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
    reviews = court.reviews.all().order_by("-created_on")
    review_count = court.reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.Court = court
            review.save()
            messages.add_message (
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
                )

    review_form = ReviewForm()

    return render(
    request,
    "courts/court_detail.html",
    {
        "court": court,
        "reviews": reviews,
        "review_count": review_count,
        "review_form": review_form,
    }
)