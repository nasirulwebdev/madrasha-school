from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    notice_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    class_name = models.CharField(
        max_length=100,
        default="General"   # 🔴 এটা MUST
    )

    

    def __str__(self):
        return self.title
    