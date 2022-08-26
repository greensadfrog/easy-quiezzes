from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["id"]

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id"]

    title = models.CharField(max_length=255, default="New Quiz")
    category = models.ForeignKey(Category, default=1, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    class Meta:
        abstract = True

    date_updated = models.DateTimeField(verbose_name=_("Last updated"), auto_now=True)


class Question(Updated):
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["id"]

    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.PROTECT)
    question_type = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of Question"))
    question_text = models.TextField(max_length=1000, verbose_name=_("Question Text"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))

    def __str__(self):
        return self.question_text


class Answer(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]

    question = models.ForeignKey(Question, related_name='question', on_delete=models.PROTECT)
    answer_text = models.TextField(max_length=1000, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)
