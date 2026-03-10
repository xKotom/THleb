from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField('Имя или псевдоним', max_length=100, blank=True)
    card_number = models.CharField('Номер клубной карты', max_length=50, unique=True)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    photo = models.ImageField('Фото', upload_to='photos/', null=True, blank=True)
    bio = models.TextField('О себе', blank=True)
    bonus_points = models.IntegerField('Бонусы', default=0)

    def __str__(self):
        return self.nickname or self.username


class ProfileTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField('Тег', max_length=100)

    class Meta:
        unique_together = ('user', 'tag')

    def __str__(self):
        return self.tag


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    product = models.CharField('Товар', max_length=200)
    date = models.DateTimeField('Дата', auto_now_add=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.product} — {self.price} руб.'


class Event(models.Model):
    name = models.CharField('Название', max_length=200)
    date = models.DateTimeField('Дата')
    description = models.TextField('Описание', blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user} -> {self.event}'
