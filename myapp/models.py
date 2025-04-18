from django.db import models
from django.contrib.auth.models import User

class GuestbookEntry(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ 작성자 추가
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
