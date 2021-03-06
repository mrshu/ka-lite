from django import forms
from django.forms import ModelForm, ChoiceField, RadioSelect

from contact.models import Contact, Deployment, Support, Info, Contribute

class Html5EmailInput(forms.TextInput):
    """adding email attributes"""
    input_type = 'email'
        

class ContactForm(ModelForm):
    required_css_class = 'required'
    ip = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Contact
        fields = ('name', 'email', 'org_name', 'type', "ip")
        widgets = {
            'name': forms.TextInput(attrs={ 'required': 'true' }),
            'email': Html5EmailInput(attrs={ 'required': 'true' }),
            'type': forms.Select(attrs={ 'required': 'true' }),
        }


class DeploymentForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Deployment
        fields = ('countries', 'internet_access', 'hardware_infrastructure', 'facilities', 'low_cost_bundle', 'other' )

class SupportForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Support
        fields = ('type', 'issue')

class InfoForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Info
        fields = ('issue',)

class ContributeForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Contribute
        fields = ('type','issue',)

