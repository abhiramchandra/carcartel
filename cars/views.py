from django.shortcuts import  get_object_or_404, render
from django.core.paginator import Paginator

from .models import Car
# Create your views here.
def cars(request):
    cars=Car.objects.order_by('-created_date')
    paginator=Paginator(Car ,3)
    page = request.GET.get('page')
    paged_cars=paginator.get_page(page)
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    context={
        'cars':paged_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'cars/cars.html',context)


def car_detail(request,id):
    single_car=get_object_or_404(Car,pk=id)
    context={
        'single_car':single_car,
    }
    return render(request,'cars/car_detail.html',context)


def search(request):
    cars=Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)
    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            cars=cars.filter(model_iexact=model)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            cars=cars.filter(city__iexact=city)
    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            cars=cars.filter(year__iexact=year)
    if 'body_style' in  request.GET:
        body_style=request.GET['body_style']
        if body_style:
            cars=cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__ite=max_price)
    context={
        'cars':cars
    }
    return render(request,'cars/search.html',context)