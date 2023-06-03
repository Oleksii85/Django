from django.db import models
import datetime


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"


class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogposts')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    def get_time(self):
        return f"{datetime.datetime.today()}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class Comment(models.Model):
    created_at = models.DateField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.content}"

    def get_time(self):
        return f"{datetime.datetime.today()}"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    blogpost = models.ManyToManyField(Blogpost)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Top"
        verbose_name_plural = "Top"
