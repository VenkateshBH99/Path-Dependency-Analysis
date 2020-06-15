from django import forms
from generate.models import Predictions

class Predict_Form(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = ('filename',)
        widgets = {'filename': forms.TextInput(attrs={'class': 'form-control'}),
                   #  'CFG_image': forms.ImageField(max_length=20),
                   # 'PDA_image': forms.ImageField(max_length=20),
                   # 'SCC_image': forms.ImageField(max_length=20),

                   }
