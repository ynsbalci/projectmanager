from django.shortcuts import render, redirect
from .models import Work, Task, Employee
from .forms import AddForm
from django.contrib import messages


# Create your views here.
def work_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    task_list = Task.objects.all()
    employee_list = Employee.objects.all()
    work_list = Work.objects.all()

    context = {
        'task_list': task_list,
        'employee_list': employee_list,
        'work_list': work_list,
    }
    return render(request, 'work/index.html', context)


def add_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    form = AddForm(request.POST or None)
    if form.is_valid():
        work = form.save(commit=False)
        work.w_employee = request.user
        work.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        # return HttpResponseRedirect(fault.get_absolute_url()) # yapılcak
        # return reverse('fault:index', {})
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, "work/add.html", context)
