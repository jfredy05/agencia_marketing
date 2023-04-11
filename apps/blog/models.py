from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    views = models.IntegerField(default=0, blank=True)
    parent = models.ForeignKey(
        "self", related_name='children',
        on_delete=models.CASCADE, blank=True, null=True
    )
    
    def __str__(self):
        return self.name
    
    def get_view_count(self):
        views = ViewCount.objects.filter(category=self).count()
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ViewCount(models.Model):
    category = models.ForeignKey(Category, related_name='category_view_count', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.ip_address}"


def blog_thumbnail_directory(instance, filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to=blog_thumbnail_directory)
    
    excerpt = models.CharField(max_length=255)
    description = RichTextField()
    time_read = models.IntegerField()
    
    published = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('published',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'