from django import forms 
from sinimg.models import SinImg

class SinImgForm(forms.ModelForm):
    class Meta:
        model = SinImg
        fields = "__all__"
