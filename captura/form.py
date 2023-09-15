from django import forms  
from captura.models import Promovidos  
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Promovidos
        fields = "__all__"    