from django.db import models


# Create your models here.
def user_directory_path(instance, filename):
    return f'images/profile_images/{instance.first_name}/{filename}'


class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

