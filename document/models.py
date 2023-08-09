from django.db import models
from authentication.models import CustomUser
# Create your models here.

class Document(models.Model):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'DOCX'),
        ('txt', 'TXT'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_documents')

    file = models.FileField(upload_to='documents/')

    shared_with = models.ManyToManyField(CustomUser, related_name='shared_documents', blank=True)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return f"{self.title}"