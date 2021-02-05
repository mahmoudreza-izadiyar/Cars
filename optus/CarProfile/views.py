from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars
from .forms import CarEditForm


# Create your views here.
def index(request):
    cars = Cars.objects.all()

    context = {
        "cars": cars
    }
    return render(request, 'CarProfile/index.html', context)


def addCar(request):
    cars = Cars.objects.all()
    if request.method == 'POST' and request.FILES['photo']:
        name = request.POST.get('name')
        color = request.POST.get('color')
        model = request.POST.get('model')
        photo = request.FILES['photo']
        car = Cars.objects.create(name=name, color=color, model=model, photo=photo)

    context = {
        "cars": cars
    }
    return render(request, 'CarProfile/index.html', context)


def delete(request, carId):
    cars = Cars.objects.all()
    car = Cars.objects.get(id=carId)
    message = f"{car.name} has been deleted successfully"
    car.delete()

    context = {
        "message": message,
        "cars": cars
    }
    return render(request, 'CarProfile/index.html', context)


def edit(request, carId):
    car = Cars.objects.get(id=carId)
    instance = get_object_or_404(Cars, id=carId)
    form = CarEditForm(request.POST or None, request.FILES, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'car': car
    }
    return render(request, 'CarProfile/edit.html', context)


def document(request):

    return render(request, 'CarProfile/doc.html')