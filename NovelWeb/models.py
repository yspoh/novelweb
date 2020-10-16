from django.db import models


# Create your models here.
class title(models.Model):
    book_id = models.IntegerField(default=0, primary_key=True)
    book_name = models.CharField(max_length=100)
    status = models.CharField(default=False, max_length=10)
    author = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    info = models.CharField(max_length=300)
    last_update = models.CharField(max_length=30, null=True)
    last_list_id = models.IntegerField(null=True)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name


class list(models.Model):
    list_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(title, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return 'NovelList' + str(self.list_id)


class rank(models.Model):
    book = models.ForeignKey(title, on_delete=models.CASCADE)
    place = models.IntegerField(null=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type
