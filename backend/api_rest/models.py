from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_path = models.TextField()

    def __str__(self):
        return f'Product: {self.id} - {self.name}'