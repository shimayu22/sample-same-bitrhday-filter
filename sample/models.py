from django.db import models

# Create your models here.
class Samplepeople(models.Model):
    """仮のモデル"""

    name = models.CharField(
        verbose_name="名前",
        max_length=5,
    )

    kana = models.CharField(
        verbose_name="かな",
        max_length=8,
    )

    date_of_birth = models.DateField(
        verbose_name="生年月日"
    )