from django.db import models


class Person(models.Model):
    class Meta:
        verbose_name_plural = "people"

    name = models.TextField()
    mnemonic = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    topics = models.TextField()
    notes = models.TextField()
    # LinkedIn URL: get the profile picture?


class Tag(models.Model):
    name = models.TextField()


class Meeting(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.DateField()
    reporter = models.ForeignKey(Person, on_delete=models.CASCADE)
