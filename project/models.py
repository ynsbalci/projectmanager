from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from employee.models import Employee


# Create your models here.
class Project(models.Model):
    p_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')#pk
    p_name = models.CharField(max_length=120, verbose_name="Name")
    p_defination = models.TextField(verbose_name="Defination")
    p_type = models.CharField(max_length=120, verbose_name="Type")
    p_begin = models.DateTimeField(verbose_name="Begin Date", auto_now_add=False)#date
    p_end = models.DateTimeField(verbose_name="End Date", auto_now_add=False)#date
    p_manager = models.ForeignKey(Employee, related_name="p_manager", on_delete=models.SET_NULL, null=True, verbose_name="Employee")
    p_status = models.IntegerField(verbose_name="Status", default=0)
    p_slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        return reverse('project:detail', kwargs={'p_slug': self.p_slug})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('project:create', kwargs={'p_slug': self.p_slug})

    def get_update_url(self):
        return reverse('project:update', kwargs={'p_slug': self.p_slug})

    def get_vote_url(self):
        return reverse('project:vote', kwargs={'p_slug': self.p_slug})

    def get_task_url(self):
        return reverse('project:task', kwargs={'p_slug': self.p_slug})

    def get_unique_slug(self):
        slug = slugify(self.p_name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Project.objects.filter(p_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.p_slug = self.get_unique_slug()
        return super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ['p_name', 'p_id']
