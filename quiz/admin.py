from django.contrib import admin
from .models import Category, Quiz, Question, Answer
from . import models


# Register your models here.

# admin.site.register(Category)
# admin.site.register(Quiz)
# admin.site.register(Question)
# admin.site.register(Answer)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


class AnswerInLineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right'
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'question_text',
        'quiz',
    ]
    list_display = [
        'question_text',
        'quiz',
        'date_updated'
    ]
    inlines = [
        AnswerInLineModel
    ]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
        ]