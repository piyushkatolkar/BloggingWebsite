from django.db import models

# Create your models here.
class post(models.Model):
    sno = models.AutoField(primary_key=True)
    # print(sno)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.SlugField(max_length=130, unique=True, null=True, blank=True)
    timeStamp = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.title + ' by ' + self.author