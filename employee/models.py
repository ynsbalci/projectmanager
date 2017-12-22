from django.db import models, connection
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Employee(AbstractUser):
    e_phone = models.CharField(blank=True, null=True, max_length=120, verbose_name="Phone")
    e_date_left = models.DateTimeField(verbose_name="Left Date", null=True, blank=True)
    # birthdate = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=range(1995, 2017)))
    e_qualification = models.CharField(default="Emloyee", max_length=120, verbose_name="Qualification")
    e_salary_rate = models.FloatField(blank=True, null=True, verbose_name="Salary")  # float maaş yüzde
    e_slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.username


    def get_absolute_url(self):
        return reverse('employee:detail', kwargs={'e_slug': self.e_slug})
        # return "/post/{}".format(self.id)


    def get_create_url(self):
        return reverse('employee:create', kwargs={'e_slug': self.e_slug})


    def get_update_url(self):
        return reverse('employee:update', kwargs={'e_slug': self.e_slug})

    def get_unique_slug(self):
        slug = slugify(self.username.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Employee.objects.filter(e_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug


    def save(self, *args, **kwargs):
        self.e_slug = self.get_unique_slug()
        return super(Employee, self).save(*args, **kwargs)

    class Meta:
        ordering = ['username', 'id']

    # stored pro
    @staticmethod
    def search(search_string):
        # create a cursor
        cur = connection.cursor()
        # execute the stored procedure passing in
        # search_string as a parameter
        cur.callproc('searcher_document_search', [search_string, ])
        # grab the results
        results = cur.fetchall()
        cur.close()

        # wrap the results up into Document domain objects
        return [Employee(*row) for row in results]

    #with connection.cursor() as cursor:
        #cursor.callproc('test_procedure', [1, 'test'])



