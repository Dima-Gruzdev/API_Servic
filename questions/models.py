from django.db import models


class Question(models.Model):
    text = models.TextField(help_text="Описание вопроса")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text[:50]
