from django.shortcuts import render
from . import models
from django.db.models import Avg, Max, Min,Aggregate
# Create your views here.
def home(request):
    data=models.db.objects.all()
    country=models.db.objects.values_list('country',flat=True).distinct()
    title=models.db.objects.values_list('title',flat=True).distinct()
    pestle=models.db.objects.values_list('pestle',flat=True).distinct()
    hood=models.db.objects.values_list('hood',flat=True).distinct()
    intensity=models.db.objects.values_list('intensity',flat=True).distinct()
    source=models.db.objects.values_list('source').distinct()
    relevance=models.db.objects.values_list('relevance',flat=True).distinct()
    region=models.db.objects.values_list('region',flat=True).distinct()
    sector=models.db.objects.values_list('sector',flat=True).distinct()
    filter_year=models.db.objects.filter(end_year=2018)
    end_year=models.db.objects.values_list('end_year',flat=True).order_by('end_year').distinct()
    topic=models.db.objects.values_list('topic',flat=True).distinct()
    context={'data':data,'country':country,'source':source,'topic':topic,'sector':sector,'title':title,'hood':hood,'intensity':intensity,'region':region,'relevance':relevance,'end':end_year,'filter_year':filter_year,'pestle':pestle}
    return render(request,'charts/home.html',context=context)