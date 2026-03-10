from django.db import models
from django.conf import settings


class Feedback(models.Model):
    TYPE_CHOICES = [
        ('complaint', 'Жалоба'),
        ('praise', 'Похвала'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks')
    type = models.CharField('Тип', max_length=10, choices=TYPE_CHOICES)
    text = models.TextField('Текст')
    category = models.CharField('Категория', max_length=100, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.get_type_display()} от {self.user}'
