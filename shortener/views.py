
from os import link
from .models import Url
import uuid
from django.http import HttpResponse
from django.shortcuts import redirect, render

from shortener.models import Url

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
   if request.method=='POST':
       link=request.POST['link']
       uid=(uuid.uuid4())[:5]
       new_url=Url(link=link,uuid=uid)
       new_url.save()
       return HttpResponse(uid)
def go(request,pk):
    url_details=Url.objects.get(uuid=pk)
    
    return redirect(url_details.link)

