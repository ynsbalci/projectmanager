from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from project.models import Project


# Create your models here.
class Task(models.Model):
    t_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')
    t_project = models.ForeignKey(Project, related_name="t_project", on_delete=models.SET_NULL, null=True, verbose_name="Project")
    t_name = models.CharField(max_length=120, verbose_name="Name")
    t_defination = models.TextField(verbose_name="Defination")
    t_begin = models.DateTimeField(verbose_name="Begin Date", auto_now_add=True)
    t_end = models.DateTimeField(verbose_name="End Date", auto_now_add=False)
    t_status = models.IntegerField(verbose_name="Status", default=0)
    t_slug = models.SlugField(unique=True, editable=False, max_length=130)


    def __str__(self):
        return self.t_name

    def get_absolute_url(self):
        return reverse('task:detail', kwargs={'t_slug': self.t_slug})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('task:create', kwargs={'t_slug': self.t_slug})

    def get_update_url(self):
        return reverse('task:update', kwargs={'t_slug': self.t_slug})

    def get_work_url(self):
        return reverse('task:work', kwargs={'t_slug': self.t_slug})

    def get_fault_url(self):
        return reverse('task:fault', kwargs={'t_slug': self.t_slug})

    def get_unique_slug(self):
        slug = slugify(self.t_name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Task.objects.filter(t_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.t_slug = self.get_unique_slug()
        return super(Task, self).save(*args, **kwargs)

    class Meta:
        ordering = ['t_name', 't_id']
