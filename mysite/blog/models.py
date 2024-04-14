from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    # created y updated son campos que se actualizan automáticamente cuando se crea o modifica un registro
    # create tomara la fecha y hora actual cuando se cree un registro
    created = models.DateTimeField(auto_now_add = True)
    # updated tomara la fecha y hora actual cuando se modifique un registro
    updated = models.DateTimeField(auto_now = True)
    # 
    status = models.CharField(max_length = 2,
                            choices = Status.choices,
                            default = Status.DRAFT)
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title