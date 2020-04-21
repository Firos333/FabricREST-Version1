import psycopg2
import datetime 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PrimaryTable,FaultTable,MasterTable
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db import connection
from django.db.models import Max
# Create your views here.

global meter1   
global Unique_id 
global my_list
my_list=[]
def index(request):
    global Unique_id 
    if request.method == 'POST':
        loom_no = request.POST['loom_no']
        piece_no = request.POST['piece_no']
        set_no = request.POST['set_no']
        beam_no = request.POST['beam_no']
        primary=PrimaryTable()
        primary.save()
        Unique_id = str(primary.pk)+loom_no+str(piece_no)+str(set_no)
        verthe=primary.pk
        primary=PrimaryTable(loom_no=loom_no,piece_no=piece_no,set_no=set_no,beam_no=beam_no,Unique_id=Unique_id )
        primary.pk = verthe
        # primary.save(update_fields=["Unique_id"]) 
        primary.save()
        # primary = PrimaryTable.objects.get(primary.pk-1)
        # primary.save(force_update=True) 
        return redirect('meter')
    else:
        return render(request,'index.html')

def meter(request):
    global Unique_id
    global meter1 
    if "submit" in request.POST:
        meter = request.POST['meter']
        meter1=meter
        messages.info(request,'Thanks, your meter log updated')
        return redirect('meter')
    elif "save" in request.POST:
        maxx=FaultTable.objects.filter(Unique_id=Unique_id).aggregate(Max('meter'))
        y=maxx.get("meter__max")
        for x in range (1,y+1):
            meter=x
            wdr_count = FaultTable.objects.filter(meter=x,Unique_id=Unique_id, fault='wdr').count()
            wdt_count = FaultTable.objects.filter(meter=x, Unique_id=Unique_id,fault='wdt').count()
            cm_count = FaultTable.objects.filter(meter=x,Unique_id=Unique_id, fault='cm').count()
            cwp_count = FaultTable.objects.filter(meter=x,Unique_id=Unique_id, fault='cwp').count()
            sos_count = FaultTable.objects.filter(meter=x,Unique_id=Unique_id, fault='sos').count()
            sv_count = FaultTable.objects.filter(meter=x, Unique_id=Unique_id,fault='sv').count()
            second=MasterTable(wdr_count=wdr_count,wdt_count=wdt_count,cm_count=cm_count,cwp_count=cwp_count,sos_count=sos_count,sv_count=sv_count,Unique_id=Unique_id,meter=meter)
            second.save()
        messages.info(request,'report saved succussfully')
        return redirect('meter')
    else:
        return render(request,'meter.html')



def sizing(request):
    global Unique_id 
    global meter1 
    if "sos" in request.POST:
        sos = request.POST['sos']
        my_list.append(sos)
        return redirect('sizing')
    elif "sv" in request.POST:
        sv = request.POST['sv']
        my_list.append(sv)
        return redirect('sizing')
    elif "undo" in request.POST:
        my_list.pop()
        return redirect('sizing')
    elif "back" in request.POST:
        for ft in my_list:
            fault=ft
            third=FaultTable(fault=fault,meter=meter1,Unique_id =Unique_id )
            third.save()
        my_list.clear()
        return redirect('meter')
    else:
        return render(request,'sizing.html')

def yawn(request):
    global Unique_id 
    global meter1 
    if "cm" in request.POST:
        cm = request.POST['cm']
        my_list.append(cm)
        return redirect('yawn')
    elif "cwp" in request.POST:
        cwp = request.POST['cwp']
        my_list.append(cwp)
        return redirect('yawn')
    elif "undo" in request.POST:
        my_list.pop()
        return redirect('yawn')
    elif "back" in request.POST:
        for ft in my_list:
            fault=ft
            third=FaultTable(fault=fault,meter=meter1,Unique_id =Unique_id )
            third.save()
        my_list.clear()
        return redirect('meter')
    else:
        return render(request,'yawn.html')


def weaver(request):
    global Unique_id 
    global meter1 
    if "wdr" in request.POST:
        wdr = request.POST['wdr']
        my_list.append(wdr)
        return redirect('weaver')
    elif "wdt" in request.POST:
        wdt = request.POST['wdt']
        my_list.append(wdt)
        return redirect('weaver')
    elif "undo" in request.POST:
        my_list.pop()
        return redirect('weaver')
    elif "back" in request.POST:
        for ft in my_list:
            fault=ft
            third=FaultTable(fault=fault,meter=meter1,Unique_id =Unique_id )
            third.save()
        my_list.clear()
        return redirect('meter')
    else:
        return render(request,'weaver.html')


# wdr_count = FaultTable.objects.filter(meter=meter1, wdr=wdr).count()