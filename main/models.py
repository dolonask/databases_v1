from django.db import models
from django.contrib.auth.models import User
from migrant.models import Country as Countries


# Create your models here.
class Country(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь', related_name='country')
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, verbose_name='Страна')

    def __str__(self):
        return self.country.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Role(models.Model):
    name = models.CharField('Позиция', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Position(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True, related_name='position')
    role = models.ForeignKey(Role, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Позиция')

    # def __str__(self):
    #     return self.role.name

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'
        