from django.shortcuts import render, redirect, get_object_or_404

from .models import Albamon

# Create your views here.

def main(request):
    albamon = Albamon.objects.all()
    context = {
        'albamon': albamon
    }
    return render(request, 'main.html', context)

def detail(request, id):
    detail_data = get_object_or_404(Albamon, pk=id)
    context = {
        'brand' : detail_data.brand,
        'area' : detail_data.area,
        'requirement' : detail_data.requirement,
        'wage' : detail_data.wage,
        'job' : detail_data.job,
        'number' : detail_data.number,
        'id' : id
    }
    return render(request, 'detail.html', context)

def create_page(request):
    return render(request, 'create.html')

def create(request):
    new_data = Albamon()
    new_data.brand = request.POST['brand']
    new_data.area = request.POST['area']
    new_data.requirement = request.POST['requirement']
    new_data.wage = request.POST['wage']
    new_data.job = request.POST['job']
    new_data.number = request.POST['number']
    new_data.save()
    return redirect('main')

def update_page(request, id):
    update_data = get_object_or_404(Albamon, pk=id)
    context = {
        'id' : id, 
        'brand' : update_data.brand,
        'area' : update_data.area,
        'requirement' : update_data.requirement,
        'wage' : update_data.wage,
        'job' : update_data.job,
        'number' : update_data.number,
    }
    return render(request, 'update.html', context)

def update(request, id):
    update_data = get_object_or_404(Albamon, pk=id)
    update_data.brand = request.POST['brand']
    update_data.area = request.POST['area']
    update_data.requirement = request.POST['requirement']
    update_data.wage = request.POST['wage']
    update_data.job = request.POST['job']
    update_data.number = update_data.number
    update_data.save()
    return redirect('main')

def delete(request, id):
    delete_data = get_object_or_404(Albamon, pk=id)
    delete_data.delete()
    return redirect('main')

def plus(request, id):
    plus_data = get_object_or_404(Albamon, pk=id)
    plus_data.number +=1
    plus_data.save()
    return redirect('detail', id)

def minus(request, id):
    minus_data = get_object_or_404(Albamon, pk=id)
    minus_data.number -=1
    minus_data.save()
    return redirect('detail', id)