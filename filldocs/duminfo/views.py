from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DumUser
from django.urls import reverse
from django.contrib.auth.models import User
from .formDicts import formDict,formName
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
import os
import random
from random import randint
from datetime import datetime
import zipfile
from filldocs.ceti_dict import formPhDict,necdict

# Create your views here.
from .forms import *

# class dumCreate(CreateView):
#     model = DumUser
#     template_name ='duminfo/dum_forms.html'
#     fields = '__all__'
#     success_url = '/accounts/dummy.html/'
#
#     def __init__(self,user,necFields,*args,**kwargs):
#         super(dumCreate,self).__init__(*args,**kwargs)
#         for f in self.fields:
#             if f not in necFields:
#                 del self.fields[f]
#
#
#
#     def get_context_data(self, **kwargs):
#         ctx = super(dumCreate,self).get_context_data(**kwargs)
#         ctx['head1'] = 'Your First Information'
#         return ctx

# formDict = {
#     1:DumUserForm1,
#     2:DumUserForm2,
# }
#
# formName = {
#     1:'MyForm',
#     2:'dummyForm',
# }
@login_required(login_url='/accounts/login/')
def updatedum(request,id):

    user = request.user
    du = user.dumuser
    id = int(id)


    formT = formDict.get(id,formDict[2])


    if request.method == 'POST':
        form = formT(request.POST, instance=du)

        if form.is_valid():
            form.save()
            newurl = '/duminfo/form'+str(id)+'/getForm'
            return redirect(newurl)
    else:
        form = formT(instance=du)

        args = {'head1': formName.get(id,'UnknownForm'),'form': form}
        return render(request, 'duminfo/dum_forms.html', args)


@login_required(login_url='/accounts/login/')
def viewPdf(request,id):
    random.seed(datetime.now())
    filename=str(request.user.id) +'_'+str(id)
    dirname = str(request.user.id) +'_'+ str(randint(100000,999999))
    formroot = 'duminfo/static/duminfo/'
    dirpath = formroot+"/sessFolder/"+dirname
    orgname = formroot+'orgForm/'+'Form'+str(id)+'.odt'
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    zip_ref = zipfile.ZipFile(orgname, 'r')
    zip_ref.extractall(dirpath)
    zip_ref.close()
    du = request.user.dumuser
    necFields = necdict.get(int(id),necdict[1])

    contFile = open(dirpath+'/content.xml','r')
    allLines = contFile.read()
    contFile.close()

    for fl in necFields:
        allLines= allLines.replace(formPhDict[fl],str(getattr(du,fl)))

    contFile = open(dirpath + '/content.xml', 'w')
    contFile.writelines(allLines)
    contFile.close()
    # command1 = 'zip -r '+dirpath+'/Final.odt '+dirpath+'/mimetype '+dirpath+'/*'
    command1 = 'bash createodt.sh '+dirpath+'/'
    # print (command1)
    os.system(command1)
    # os.system('ls')
    pdfpath = 'duminfo/sessFolder/'+dirname+'/final.pdf'
    # 'duminfo/google.pdf'


    args={'head1': formName.get(int(id),'UnknownForm'),'path':pdfpath}
    return render(request, 'duminfo/dum_pdfdis.html',args)


