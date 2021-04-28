from django.db import models
from django.conf import settings
# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length= 500)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()
    def __str__(self):
        return self.title
class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length= 500)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Answers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Questions, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.choice.title