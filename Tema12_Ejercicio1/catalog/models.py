from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text='Descripción de la película')

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.surname
