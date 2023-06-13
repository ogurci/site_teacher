from django.db import models

class Teory1(models.Model):
    title = models.CharField('Название', max_length=50)
    file = models.FileField('Документ', upload_to='static/main/file')

    def __str__(self):
        return self.title

class Practic1(models.Model):
    title = models.CharField('Название', max_length=50)
    file = models.FileField('Документ', upload_to='static/main/file')

    def __str__(self):
        return self.title

class Teory2(models.Model):
    title = models.CharField('Название', max_length=50)
    file = models.FileField('Документ', upload_to='static/main/file')

    def __str__(self):
        return self.title

class Practic2(models.Model):
    title = models.CharField('Название', max_length=50)
    file = models.FileField('Документ', upload_to='static/main/file')

    def __str__(self):
        return self.title


class Nagrad(models.Model):
    title = models.CharField('Название', max_length=50)
    file = models.FileField('Документ', upload_to='static/main/file')

    def __str__(self):
        return self.title
