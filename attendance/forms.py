from django import forms
from .models import UserProfile

class UserPForm(forms.ModelForm):
	username = forms.CharField(max_length=128)
	department = forms.CharField(max_length=10)
	year=forms.IntegerField()
	

	class Meta:
		model = UserProfile
		fields = ('username','Department','Year')

