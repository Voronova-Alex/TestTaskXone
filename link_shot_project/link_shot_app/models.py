from django.db import models
from django.contrib.auth.models import User

class Links(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Имя")
    input_link = models.URLField(verbose_name='Ссылка')
    output_link = models.CharField(max_length=15, unique=True, blank=True, verbose_name='Короткая ссылка')
    date_create_link = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
