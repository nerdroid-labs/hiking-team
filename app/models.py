from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    mountain_name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    date = models.DateField()
    participants = models.ManyToManyField(Member)

    def __str__(self):
        return f"[{self.date}] {self.mountain_name}"

class Photo(models.Model):
    file = models.ImageField(upload_to="photo/%Y/%m/%d")
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name