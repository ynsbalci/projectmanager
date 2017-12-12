from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Fault
from .forms import AddForm, UpdateForm
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def fault_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    fault_list = Fault.objects.filter()
    return render(request, 'fault/index.html', {'fault_list': fault_list})


def add_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    form = AddForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        fault = form.save(commit=False)
        fault.f_employee = request.user
        fault.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(fault.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "fault/add.html", context)


def update_view(request, f_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    fault = get_object_or_404(Fault, f_slug=f_slug)

    form = UpdateForm(request.POST or None, instance=fault)
    if form.is_valid():
        form.save()

        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(fault.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "fault/update.html", context)


def detail_view(request, f_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    fault = get_object_or_404(Fault, f_slug=f_slug)
    context = {
        'fault': fault,
    }
    return render(request, "fault/detail.html", context)


