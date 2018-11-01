from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DumUser
from django.urls import reverse
from django.contrib.auth.models import User
from .formDicts import formDict,formName
from django.contrib.auth.decorators import login_required


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
    args={'head1': formName.get(id,'UnknownForm'),'path':'./google.pdf'}
    return render(request, 'accounts/dummy.html',args)





