from django.shortcuts import get_object_or_404, redirect, render
from .formsc import CategoryForm


def index(request):
    return render(request, 'shop/index.html')

def category(request):
    return render(request, 'shop/category.html', {
        'category': category,
    })
