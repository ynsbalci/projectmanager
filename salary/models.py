from django.db import models
from django.urls import reverse
from employee.models import Employee
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Salary(models.Model):
    s_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')
    s_date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    s_voter = models.ForeignKey(Employee, related_name="s_voter", on_delete=models.CASCADE, verbose_name="Voter")
    s_choise = models.ForeignKey(Employee, related_name="s_choise", on_delete=models.SET_NULL, null=True, verbose_name="Choise")
    s_vote = models.FloatField(verbose_name="Vote")

    def get_update_url(self):
        return reverse('salary:index')
        # return "/post/{}".format(self.id)

@receiver(post_save, sender=Salary)
def signal(sender, **kwargs):
     if kwargs.get('created', False):
         # print(kwargs)
         # print(kwargs.get('instance'))
         # print(kwargs.get('s_vote'))
         employee_list = Employee.objects.all()
         salary_list = Salary.objects.filter()

         for employee in employee_list:
            print(employee)
            rate = 0
            count = 0
            for salary in salary_list:
                 print(salary.s_choise)
                 if employee == salary.s_choise:
                     print("buldum")
                     count = count + 1
                     rate += salary.s_vote
                     employee.e_salary_rate = rate / count
                     employee.save()




