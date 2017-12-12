from django.shortcuts import render, redirect
from employee.models import Employee
from task.models import Task
from project.models import Project


# Create your views here.
def home_view(request):
    return render(request, 'home/index.html', {})


def pdf_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    employee_list = Employee.objects.all()
    task_list = Task.objects.all()
    project_list = Project.objects.all()

    context = {
        'employee_list': employee_list,
        'task_list': task_list,
        'project_list': project_list,
    }

    return render(request, "home/pdf.html", context)

from reportlab.pdfgen import canvas
from django.http import HttpResponse


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='home/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


