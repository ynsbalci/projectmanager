from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Task
from work.models import Work
from employee.models import Employee
from .forms import AddForm, UpdateForm, TaskWorkForm, TaskFaultForm
from django.contrib import messages


# Create your views here.
def task_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    task_list = Task.objects.filter(t_status=1)
    work_list = Work.objects.filter(w_employee=request.user)

    for work in Work.objects.filter(w_employee=request.user):
        print(work.w_task)
        print(work.w_employee)

    context = {
        'task_list': task_list,
        'work_list': work_list,
    }

    return render(request, 'task/index.html', context)


def confirm_task_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    task_list = Task.objects.filter(t_status=0)
    work_list = Work.objects.filter(w_task=task_list, w_employee=request.user)
    employee = Employee.objects.filter()

    context = {
        'task_list': task_list,
        'work_list': work_list,
        'employee': employee,
    }
    return render(request, 'task/confirm.html', context)


def task_work(request, t_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    task = get_object_or_404(Task, t_slug=t_slug)
    # work = Work.objects.filter(v_voter=request.user)
    form = TaskWorkForm(request.POST or None)
    if form.is_valid():
        work = form.save(commit=False)
        work.w_task = task
        work.w_employee = request.user
        work.save()
        task.t_status = 1
        task.save()
        messages.success(request, "Başarılı bir şekilde oyladınız.")
        return HttpResponseRedirect(task.get_absolute_url())

    context = {

        'task': task,
        'form': form
    }

    return render(request, "task/fault.html", context)

def task_fault(request, t_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    task = get_object_or_404(Task, t_slug=t_slug)
    # work = Work.objects.filter(v_voter=request.user)
    form = TaskFaultForm(request.POST or None)
    if form.is_valid():
        fault = form.save(commit=False)
        fault.f_task = task
        fault.f_employee = request.user
        fault.save()
        messages.success(request, "Başarılı bir şekilde oyladınız.")
        return HttpResponseRedirect(task.get_absolute_url())

    context = {

        'task': task,
        'form': form
    }

    return render(request, "task/fault.html", context)

def create_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    form = AddForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(task.get_absolute_url()) # yapılcak

    context = {
        'form': form
    }

    return render(request, "task/add.html", context)


def detail_view(request, t_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    task = get_object_or_404(Task, t_slug=t_slug)
    context = {
        'task': task,
    }
    return render(request, "task/detail.html", context)


def update_view(request, t_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    task = get_object_or_404(Task, t_slug=t_slug)

    form = UpdateForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(task.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "task/update.html", context)