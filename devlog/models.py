from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# https://blog.finxter.com/how-i-created-a-blog-application-using-django/

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devlog_posts')
    title = models.CharField(max_length=255, unique=True)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering: ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('log_detail.html', kwargs({'slug':self.slug}))


