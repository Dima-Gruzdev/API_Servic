from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')
    search_fields = ('text',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
