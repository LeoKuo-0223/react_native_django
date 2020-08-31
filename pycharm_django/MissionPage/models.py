from django.db import models


# Create your models here.
class MissionPage(models.Model):
    title = models.CharField(unique=True, max_length=50, verbose_name='任務標題')
    content = models.TextField(verbose_name='任務內容')
    missiontype = models.TextField(unique=True, max_length=50, verbose_name='種類')
    missionClear = models.BooleanField(default=False, verbose_name='是否完成')
    editTime = models.DateTimeField(auto_now=True, verbose_name='Edit Time')
