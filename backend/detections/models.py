from django.db import models

class NeckDetection(models.Model):
    blob_data = models.TextField()
    face_x_mean = models.FloatField(default=0.0)
    face_y_mean = models.FloatField(default=0.0)
    nose_mean = models.FloatField(default=0.0)
    face_x = models.TextField(default=None, null=True, blank=True)
    face_y = models.TextField(default=None, null=True, blank=True)
    nose_to_center = models.TextField(default=None, null=True, blank=True)
    cnt = models.IntegerField(default=0)
    detection_flag = models.CharField(max_length=50, blank=True)

class BlinkDetection(models.Model):
    blob_data = models.TextField()
    count = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    time = models.IntegerField(default=0) # 1: 1ms
    detection_flag = models.CharField(max_length=50, blank=True)