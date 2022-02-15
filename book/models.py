from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to="book_images/", null=True)
    author = models.CharField(max_length=100)

    def get_absolute_url(self):
        return f"{self.pk}"
