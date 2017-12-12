from django.db import models
from task.models import Task
from employee.models import Employee


# Create your models here.
class Work(models.Model):
    w_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')
    w_task = models.ForeignKey(Task, related_name="w_task", on_delete=models.SET_NULL, null=True, verbose_name="Task")
    w_employee = models.ForeignKey(Employee, related_name="w_employee", on_delete=models.SET_NULL, null=True, verbose_name="Employee")


