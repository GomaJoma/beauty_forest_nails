from django.shortcuts import render
from .models import Review


def reviews(request):
    reviews_list = Review.objects.all()
    context = {
        'reviews_list': reviews_list
    }
    return render(request, 'reviews/reviews.html', context)
