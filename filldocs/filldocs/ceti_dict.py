from django.contrib.admin.widgets import AdminDateWidget
from django import forms
necdict = {1:('f1','f3','f4')}
widgetDict = {'f4':forms.DateInput(attrs={'class': 'date-input'}),'f6':forms.DateTimeInput(attrs={'class': 'date-input'}),}


def getFormWidget(id):
    tup = necdict.get(id,())
    outdic = {}
    for field in tup:
        if field in widgetDict.keys():
            outdic[field]=widgetDict[field]

    return outdic

