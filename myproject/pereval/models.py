from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    otc = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.fam} {self.name} ({self.email})"


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"


class Pereval(models.Model):
    STATUS_CHOICES = [
        ('new', 'новый'),
        ('pending', 'модератор взял в работу'),
        ('accepted', 'модерация прошла успешно'),
        ('rejected', 'модерация прошла, информация не принята'),
    ]

    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    level_winter = models.CharField(max_length=10, blank=True)
    level_summer = models.CharField(max_length=10, blank=True)
    level_autumn = models.CharField(max_length=10, blank=True)
    level_spring = models.CharField(max_length=10, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    class Meta:
        verbose_name = "Перевал"
        verbose_name_plural = "Перевалы"


class PerevalImage(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='pereval_images/')
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изображение перевала"
        verbose_name_plural = "Изображения перевалов"