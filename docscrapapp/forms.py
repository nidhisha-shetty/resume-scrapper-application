from django import forms
from .models import Scrapper

class ScrapperForm(forms.ModelForm):
    class Meta:
        model = Scrapper
        fields = [
            'resume_file'
		] 