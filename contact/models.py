from django.db import models
from django.utils import timezone


# Create your models here.
class QuestionTag(models.Model) :
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Question Tag"
        verbose_name_plural = "Question Tags"
        ordering = ('name', 'description')

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    tags = models.ManyToManyField(QuestionTag, related_name="Tags")
    time = models.DateTimeField(default=timezone.now)

    class Meta :
        verbose_name = "Contact Question"
        verbose_name_plural = "Contact Questions"
        ordering = ('name', 'subject')

    def __str__(self):
        return self.name
