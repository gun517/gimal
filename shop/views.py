from django.shortcuts import get_object_or_404, redirect, render
from .forms import CategoryForm


def index(request):
    return render(request, 'shop/index.html')

def category(request):
    return render(request, 'shop/category.html', {
        'category': category,
    })

def category_new(request):
    if request.method == 'POST':
        form = request.POST['title']
        if form.is_valid():
            title = form.save()
            return redirect('shop/index.html')
    else:
        form = CategoryForm()
    return render(request, 'shop/category.html', {
        'form': form,
    })