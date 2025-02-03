from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=50)


class BodyPart(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=1024)
    mediaPath = models.FilePathField()


class Exercises(models.Model):
    DIFFICULTIES = [
        ("1", "Easy"),
        ("2", "Medium"),
        ("3", "Difficult"),
        ("4", "Hard"),
    ]
    name = models.CharField(max_length=50)
    bodyPartId = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
    mediaPath = models.FilePathField()
    difficulty = models.CharField(max_length=1, choices=DIFFICULTIES)
    equipment = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tags)
