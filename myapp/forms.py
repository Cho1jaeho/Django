from django import forms
from .models import GuestbookEntry

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '이름'}),
            'message': forms.Textarea(attrs={'placeholder': '메시지를 입력하세요'}),
        }
