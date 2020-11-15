from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save() # Run save method of parent class
        
        img = Image.open(self.image.path) # Open image of current instance

        max_height = 300
        max_width = 300

        if img.height > max_height or img.width > max_width:
            output_size = (max_height, max_width)
            img.thumbnail(output_size)
            img.save(self.image.path)