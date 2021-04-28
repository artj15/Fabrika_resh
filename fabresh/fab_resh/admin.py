from django.contrib import admin
from .models import Questions, Answers, Choice
# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points'
    )
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'points',
        'lock_other'
    )
    list_filter = ('question', )

class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
        'created'
    )
    # readonly_fields = ('created', )
    list_filter = ('user', )
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers, AnswerAdmin)
admin.site.register(Choice, ChoiceAdmin)
