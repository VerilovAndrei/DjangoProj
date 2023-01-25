import os

from django.db import models

class Profession (models.Model):
    title = models.CharField('Назввание',max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Професcия"
        verbose_name_plural = 'Профессии'

class Image (models.Model):
    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = ""
        return os.path.join("images", filename)
        title = models.CharField('Назввание',max_length=50)
        description = models.TextField('Описание')
        photo = models.ImageField(verbose_name=u'Poster', upload_to= get_file_path, max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = 'Фото'

