from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from employee.models import Employee
from task.models import Task


# Create your models here.
class Fault(models.Model):
    f_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')
    f_name = models.CharField(max_length=120, verbose_name="Name")
    f_task = models.ForeignKey(Task, related_name="f_task", on_delete=models.SET_NULL, null=True, verbose_name="Task")
    f_defination = models.TextField(verbose_name="Defination")
    f_date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    f_employee = models.ForeignKey(Employee, related_name="f_employee", on_delete=models.SET_NULL, null=True, verbose_name="Employee")
    f_status = models.IntegerField(verbose_name="Status", default=0)
    f_slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.f_name

    def get_absolute_url(self):
        return reverse('fault:detail', kwargs={'f_slug': self.f_slug})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('fault:create', kwargs={'f_slug': self.f_slug})

    def get_update_url(self):
        return reverse('fault:update', kwargs={'f_slug': self.f_slug})

    def get_unique_slug(self):
        slug = slugify(self.f_name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Fault.objects.filter(f_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.f_slug = self.get_unique_slug()
        return super(Fault, self).save(*args, **kwargs)

    class Meta:
        ordering = ['f_name', 'f_id']

