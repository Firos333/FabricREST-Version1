import datetime 
import uuid
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone

# Create your models here.

class PrimaryTable(models.Model):
    
    # my_id = models.IntegerField(default=0,primary_key=True)
    Unique_id = models.CharField(max_length =50,default=0,unique=True)
    loom_no = models.CharField(max_length =50,default=0)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # loom_no = models.CharField(max_length =200,primary_key=True,default=0)
    set_no = models.IntegerField(default=0)
    beam_no = models.IntegerField(default=0)
    piece_no = models.IntegerField(default=0)
    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    # class Meta:
    #     unique_together = (('id', 'loom_no'),)
    
    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         self.pk=s
    #     else:
    #         super(PrimaryTable, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.Unique_id


class MasterTable(models.Model):
    
    Unique_id = models.CharField(max_length =50,default=0)
    meter = models.IntegerField(default=0)
    wdr_count = models.IntegerField(default=0)
    wdt_count = models.IntegerField(default=0)
    cm_count = models.IntegerField(default=0)
    cwp_count = models.IntegerField(default=0)
    sos_count = models.IntegerField(default=0)
    sv_count = models.IntegerField(default=0)
    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)

class FaultTable(models.Model):
    Unique_id = models.CharField(max_length =50,default=0)
    # Unique_id = models.ForeignKey(PrimaryTable, blank =True,on_delete=models.CASCADE)
    meter = models.IntegerField(default=0)
    fault = models.CharField(max_length =50,default=0)
    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    def __str__(self):
        return self.meter