from django.shortcuts import render, redirect
from .models import Review
from .forms import AddReviewForm


def reviews(request):
    reviews_list = Review.objects.all()

    error = ''
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        print(request.user)
        if form.is_valid():
            created_form = form.save(commit=False)
            if request.user.is_authenticated:
                created_form.author = request.user
            created_form.save()
            return redirect('reviews')
        else:
            error = 'Not valid form'
    else:
        form = AddReviewForm()

    context = {
        'reviews_list': reviews_list,
        'form': form,
        'error': error,
    }
    return render(request, 'reviews/reviews.html', context)
