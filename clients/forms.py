from django import forms  
from clients.models import Client


class ClientForm(forms.ModelForm):  
    class Meta:  
        model = Client
        fields = "__all__"  
        # fields = ['cid', 'name', 'email']