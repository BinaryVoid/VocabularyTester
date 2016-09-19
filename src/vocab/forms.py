
from django import forms


from .models import vocabulary


class vocabForm(forms.ModelForm):
    class Meta:
        model = vocabulary
        fields = [
            "title",
				 ]