from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    class_name = models.CharField(max_length=50)   # ⬅️ must
    day = models.CharField(max_length=20)          # ⬅️ must
    notice_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 🔹 Class field
    class_name = models.CharField(
        max_length=100,
        default="General",
        choices=[('General','General'), ('Class 1','Class 1'), ('Class 2','Class 2'),
                 ('Class 3','Class 3'), ('Class 4','Class 4'), ('Class 5','Class 5'),
                 ('Class 6','Class 6'), ('Class 7','Class 7'), ('Class 8','Class 8'),
                 ('Class 9','Class 9'), ('Class 10','Class 10'), ('Class 11','Class 11'),
                 ('Class 12','Class 12')]
    )

    # 🔹 Day field
    day = models.CharField(
        max_length=20,
        choices=[('Saturday','Saturday'), ('Sunday','Sunday'), ('Monday','Monday'),
                 ('Tuesday','Tuesday'), ('Wednesday','Wednesday'), ('Thursday','Thursday'),
                 ('Friday','Friday')],
        default='Saturday'
    )

    def __str__(self):
        return self.title

    