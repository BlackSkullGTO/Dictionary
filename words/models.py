from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Word(models.Model):
    word = models.CharField(max_length=30)
    translate = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    lastsuccessdate = models.DateField(blank=True, null=True)
    countsuccess = models.IntegerField(default=0)
    countfailure = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.word)

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Word.objects.create(
            word="test",
            translate="тест",
            user=instance,
        )