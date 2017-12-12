from django.shortcuts import render, redirect, get_object_or_404
from .models import Salary, Employee
from .forms import AddForm
from django.contrib import messages


# Create your views here.
def salary_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    employee_list = Employee.objects.filter(is_active=True)
    salary_list = Salary.objects.all()
    # salary = get_object_or_404(Salary)

    # form = AddForm(request.POST or None, instance=salary)

    form = AddForm(request.POST or None)
    if form.is_valid():
        salary = form.save(commit=False)
        salary.s_voter = request.user
        salary.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        # return HttpResponseRedirect(fault.get_absolute_url()) # yapılcak
        # return reverse('fault:index', {})
        return redirect('home')

    context = {
        'salary_list': salary_list,
        'employee_list': employee_list,
        'form': form
    }

    return render(request, 'salary/index.html', context)


def add_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    form = AddForm(request.POST or None)
    if form.is_valid():
        salary = form.save(commit=False)
        salary.s_voter = request.user
        salary.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        # return HttpResponseRedirect(fault.get_absolute_url()) # yapılcak
        # return reverse('fault:index', {})
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, "salary/add.html", context)

