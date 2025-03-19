from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Court, Review
from .forms import ReviewForm
from .forms import CourtForm
from django.utils.text import slugify


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
            messages.add_message(
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


def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Court.objects.filter(status=1)
        court = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.court = court
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!'
            )

    return HttpResponseRedirect(reverse('court_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Court.objects.filter(status=1)
    court = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!'
        )

    return HttpResponseRedirect(reverse('court_detail', args=[slug]))


def add_court(request):
    if request.method == "POST":
        form = CourtForm(request.POST, request.FILES)
        if form.is_valid():
            court = form.save(commit=False)
            court.author = request.user  # Assign logged-in user as author
            court.slug = slugify(court.title)  # Generate slug from title
            # Ensure slug is unique
            counter = 1
            original_slug = court.slug
            while Court.objects.filter(slug=court.slug).exists():
                court.slug = f"{original_slug}-{counter}"
                counter += 1
            court.save()
            messages.success(
                request,
                "Your court has been submitted and is awaiting approval!"
            )  # Success message
            return redirect("home")  # Redirect to homepage or court list
    else:
        form = CourtForm()

    return render(request, "courts/add_court.html", {"form": form})
