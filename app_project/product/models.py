from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    '''Модель продукта.'''

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    name = models.CharField('Название продукта',
                            max_length=255)
    date_create = models.DateTimeField('Дата создания',
                                        auto_now_add=True)
    date_start = models.DateField('Дата старта')
    price = models.DecimalField('Стоимость в рублях',
                                max_digits=8,
                                decimal_places=2)
    min_users = models.PositiveSmallIntegerField(
        'Мин.кол-во участников в группе',
        default=1
    )
    max_users = models.PositiveSmallIntegerField(
        'Макс.кол-во участников в группе',
        default=5
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models.Model):
    '''Модель урока.'''

    title = models.CharField('Название',
                             max_length=255)
    video_link = models.URLField('Ссылка на видео',
                                 max_length=255)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Group(models.Model):
    '''Модель группы.'''

    students = models.ManyToManyField(User)
    name = models.CharField('Название',
                             max_length=255)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='groups')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class ProductAccess(models.Model):
    '''Модель доступа для пользователя к продукту при условии его покупки.'''

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    is_paid = models.BooleanField('Оплачен',
                                  default=False)
    class Meta:
        verbose_name = 'Доступ к продукту'
        verbose_name_plural = 'Доступы к продуктам'