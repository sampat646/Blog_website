from django.db import models

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=130)
    # img = models.ImageField(upload_to='/images')
    def __str__(self) -> str:
        return self.title

class contact(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField(max_length=55)
    phone=models.IntegerField(max_length=12)
    desc=models.TextField()

    def __str__(self)->str:
        return self.name