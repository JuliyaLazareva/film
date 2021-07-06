from django.db import models


class MyFilmsModel(models.Model):

    name = models.CharField(verbose_name='Название фильма', max_length=40)
    img = models.ImageField(verbose_name='Постер', upload_to='static/img', blank=True)
    genre = models.ForeignKey('GenresModel', on_delete=models.PROTECT)
    year = models.DateField(verbose_name='Дата выхода', auto_now_add=False)
    rating = models.FloatField(verbose_name='Оценка', default=0)
    comment = models.TextField(verbose_name='Отзыв', max_length=200)
    date_viewed = models.DateField(verbose_name='Дата просмотра', auto_now_add=False)
    views = models.IntegerField(verbose_name='Количество просмотров', default=1)

    def __str__(self):
        return f'Название: {self.name}, Жанр: {self.genre} , Год выхода в прокат {self.year}, Просмотрен {self.views}, Моя оценка {self.rating}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['rating']


class GenresModel(models.Model):
    name = models.CharField(verbose_name='Название жанра', max_length=40)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'