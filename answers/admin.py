from django.contrib import admin
from .models import Answer

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'user_id', 'text_preview', 'created_at')
    list_filter = ('created_at', 'question')
    search_fields = ('user_id', 'text')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Answer preview'
