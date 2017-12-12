from django.db import models
from employee.models import Employee
from project.models import Project
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Vote(models.Model):

    v_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')
    v_project = models.ForeignKey(Project, related_name="v_project", on_delete=models.SET_NULL, null=True, verbose_name="Project")
    v_voter = models.ForeignKey(Employee, related_name="v_employee", on_delete=models.SET_NULL, null=True, verbose_name="Employee")
    v_vote = models.BooleanField(verbose_name="Vote", default=False)

@receiver(post_save, sender=Vote)
def signal(sender, **kwargs):
     if kwargs.get('created', False):
         project_list = Project.objects.all()
         vote_list = Vote.objects.filter()
         employee_list = Employee.objects.filter(is_active= True)

         emo_count=0
         for employee in employee_list:
             emo_count= emo_count + 1

         for project in project_list:
            print(project)
            rate = 0.0
            for vote in vote_list:
                 if vote.v_project == project:
                     #if project.p_status ==0:

                     rate += vote.v_vote
                     print(rate / emo_count)
                     print(emo_count)
                     if (rate / emo_count) > 0.8:
                         project.p_status = 1
                         project.save()

