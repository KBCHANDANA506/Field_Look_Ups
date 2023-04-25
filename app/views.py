from django.shortcuts import render
from app.models import *
# Create your views here.

def Display_Topic(request):
    LOT=Topic.objects.all()
    #LOT=Topic.objects.filter('Topic_name'='Cricket')
    
    d={'topics':LOT}
    return render(request,'Display_Topic.html',d)
def Display_Webpage(request):
    LOW=Webpage.objects.all()
    #LOW=Webpage.objects.filter(Name='Dhoni').update(Url='MSD@gmail.com')
    #LOW=Webpage.objects.all().delete()
    #LOW=Webpage.objects.filter(Name='Dhoni').delete()
    LOW=Webpage.objects.all()
    d={'web':LOW}
    return render(request,'Display_Webpage.html',d)

def Display_Access(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'Dispaly_Access.html',d)

def update_webpage(request):
    d={'web':Webpage.objects.all()}
    #update method
    LOW=Webpage.objects.filter(Name='Dhoni').update(Url='MSD@gmail.com')
    LOW=Webpage.objects.filter(Name='Ronaldo').update(Url='Ronaldo@gmail.com')
    WO=Topic.objects.get_or_create(Topic_name='Cricket')[0]
    WO.save()
    LOW=Webpage.objects.update_or_create(Name='Ronaldo',defaults={'Topic_name':WO,'Url':'Ronaldo@gmail.com'})

    return render(request,'Display_Webpage.html',d)

def update_Access(request):
    d={'access':AccessRecord.objects.all()}
    LOA=AccessRecord.objects.all()
    
    LOA=AccessRecord.objects.filter(Author='Tagore').update(Date='2023-09-17')
    LOA=AccessRecord.objects.all()
    #udate_ot_create
    AO=Webapge.objects.get_or_create(Name='Pandya')[0]
    AO.save()


    LOA=AccessRecord.objects.update_or_create(Author='Tagore',defaults={'Name':AO,'Date':'2023-04-11'})

    


    return render(request,'Dispaly_Access.html',d)