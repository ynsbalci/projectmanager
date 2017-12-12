from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, UpdateForm
from django.contrib.auth import authenticate, login, logout
from .models import Employee
from django.contrib import messages



# Create your views here.
def employee_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    employee_list = Employee.objects.filter(is_active=True)
    return render(request, 'employee/index.html', {'employee_list': employee_list})



def employee_confirm_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    employee_list = Employee.objects.filter(is_active=False)
    return render(request, 'employee/confirm.html', {'employee_list': employee_list})


def login_view(request):

    # results = Employee.search(request.GET['search_string'])

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home')

    return render(request, "employee/login.html", {"form": form})


def detail_view(request, e_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    employee = get_object_or_404(Employee, e_slug=e_slug)
    context = {
        'employee': employee,
    }
    return render(request, "employee/detail.html", context)


def profile_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    employee = get_object_or_404(Employee, username=request.user)
    context = {
        'employee': employee,
        'e_slug': employee.e_slug,
    }
    return render(request, "employee/profile.html", context)


def update_profile_view(request, e_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    employee = get_object_or_404(Employee, username=request.user, e_slug=e_slug)
    employeea = (
        'password'
    )
    form = UpdateForm(request.POST or None, instance=employee)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()

        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(employee.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "employee/update.html", context)

def logout_view(request):
    logout(request)
    return redirect('home')


#def search():

