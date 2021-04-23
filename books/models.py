from django.db import models


class BookEntity(models.Model):
    Registered = "Registered"
    Preparing = "Preparing"
    Delivering = "Delivering"
    Received = "Received"
    TYPE_CHOICES = (
        (Registered, 'Registered'),
        (Preparing, 'Preparing'),
        (Delivering, 'Delivering'),
        (Received, 'Received')
    )
    title = models.TextField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=TYPE_CHOICES, default=Registered)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
