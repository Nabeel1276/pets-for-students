from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete



class Student(models.Model):
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    numberOfCats = models.IntegerField(default=0)

    def __str__(self):
        return self.firstName + " " + self.secondName


class Cat(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Cat)
def update_number_of_cats(sender, instance, created, **kwargs):
    if created:
        student = instance.owner
        student.numberOfCats = student.cat_set.count()
        student.save()

@receiver(post_delete, sender=Cat)
def decrement_number_of_cats(sender, instance, **kwargs):
    student = instance.owner
    student.numberOfCats = student.cat_set.count()
    student.save()