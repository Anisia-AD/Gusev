from django.db import models

class Appointment(models.Model):
    name = models.CharField('ФИО', max_length=200)
    phone = models.CharField('Телефон', max_length=20)
    problem = models.TextField('Проблема')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
