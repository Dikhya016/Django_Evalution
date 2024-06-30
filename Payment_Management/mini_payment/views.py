from django.shortcuts import render,get_object_or_404
from .models import ServiceUser,Service,Subscriptions
# Create your views here.

def userlist(request):
    users=ServiceUser.objects.all()
    return render(request,'mini_payment/userlist.html',{'users':users})

def userdetails(request,id):
    user=get_object_or_404(ServiceUser,id=id)
    subscriptions=Subscriptions.objects.filter(user=user)
    return render(request,'mini_payment/userdetails.html',{'user':user,'subscriptions': subscriptions})

def servicelist(request):
    services=Service.objects.all()
    return render(request,'mini_payment/services.html',{'services':services})

def service_detail(request,typee):
    service=get_object_or_404(Service,typee=typee)
    subscriptions=Subscriptions.objects.filter(service=service)
    return render(request,'mini_payment/service_detail.html',{'service':service,'subscriptions':subscriptions})