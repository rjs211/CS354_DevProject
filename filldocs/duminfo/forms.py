from django.forms import ModelForm
from .models import DumUser
from filldocs.ceti_dict import necdict
from filldocs.ceti_dict import getFormWidget

class DumUserForm1(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[1]
        widgets = getFormWidget(1)

class DumUserForm2(ModelForm):
    # template_name = 'duminfo/dum_forms.html'

    class Meta:
        model = DumUser
        fields = necdict[2]
        widgets = getFormWidget(2)