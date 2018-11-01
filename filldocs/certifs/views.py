from django.shortcuts import render
from django.http import HttpResponse
from .models import Certif
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.


def certif_list(request):
    certifs = Certif.objects.all().order_by('id')
    return render(request,'certifs/certifs_list.html',{'certifs':certifs})


def certif_details(request, id):

    certif = Certif.objects.get(id = id)
    if certif is not None:
        return render(request,'certifs/certifs_det.html',{'certif':certif})
    else:
        raise Http404('Object Not Found')

@login_required(login_url='/accounts/login/')
def certif_request(request):
    certif = Certif.objects.get(id = id)
    uname = request.user.username
    userId = request.user.id



