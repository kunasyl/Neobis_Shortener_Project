from django.db import models
from django.utils.translation import gettext_lazy as _


class Shortener(models.Model):
    long_url = models.URLField(max_length=800, verbose_name=_('Длинная ссылка'))
    short_url = models.CharField(max_length=200, unique=True, blank=True, verbose_name=_('Короткая ссылка'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.long_url} -> {self.short_url}'
