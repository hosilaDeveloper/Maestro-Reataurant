
from django.shortcuts import render, get_object_or_404
from .models import Food, About, Category


# Create your views here.

def home_view(request):
    foods = Food.objects.all().order_by('-id')[:3]
    about = About.objects.all().first()
    categories = Category.objects.all()
    last_images = Food.objects.all().order_by('-created_at')[:1]
    category = request.GET.get('c')
    search = request.GET.get('search')
    if search:
        foods = foods.filter(name__icontains=search)
    if category:
        foods = foods.filter(category__name__exact=category)
    context = {
        'foods': foods,
        'about': about,
        'categories': categories,
        'last_images': last_images,
    }
    return render(request, 'index.html', context)


def menu_view(request):
    foods = Food.objects.all().order_by('-id')
    categories = Category.objects.all()
    cats = request.GET.get('cat')
    if cats:
        foods = foods.filter(category__name=cats)
    context = {
        'foods': foods,
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def about_view(request):
    about = About.objects.all().first()
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)


def food_detail_view(request, pk):
    food = get_object_or_404(Food, id=pk)
    context = {
        'food': food,
    }
    return render(request, 'detail.html', context)
