from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
