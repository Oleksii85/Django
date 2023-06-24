from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Topic(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    author = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Top"
        verbose_name_plural = "Top"


class Post(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    topic = models.ManyToManyField(Topic)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = slugify(self.title, self.created_at)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class Comment(models.Model):
    created_at = models.DateField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.content}"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
