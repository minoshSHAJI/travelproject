from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import superheros

# Create your views here.
def home(request):
    obj=place.objects.all()
    sup=superheros.objects.all()
    return render(request,"index.html", {'result': obj, 'mino': sup})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     q=int(request.GET['num3'])
#     r=int(request.GET['num4'])
#     ans=q-r
#     x1=int(request.GET['num5'])
#     y1=int(request.GET['num6'])
#     an=x1*y1
#     x2=int(request.GET['num7'])
#     y2=int(request.GET['num8'])
#     answ=x2/y2
#     return render(request,"result.html",{'result':res,'result1':ans,'result2':an,'result3':answ})
# def contact(request):
#     return render(request,"result.html")
# def detail(request):
#     return HttpResponse("Cemetry Juction Ayyapankavu")
# def thanks(request):
#     return render(request,"thanks.html")