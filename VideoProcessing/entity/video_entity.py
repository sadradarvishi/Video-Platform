from django.db import models

from VideoProcessing.entity.user_entity import UserEntity

class VideoEntity(models.Model):

    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('completed', 'completed'),
        ('failed', 'failed'),
    ]

    title = models.CharField(max_length=225, null=False)
    creator = models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    processed_file = models.FileField(upload_to='processed/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', null=False, blank=False)

    def __str__(self):
        return self.title