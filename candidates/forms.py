from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from candidates.models import Candidate, Tag, Value


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required')
    last_name = forms.CharField(max_length=30, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1')


class ValueForm(forms.ModelForm):
    name = forms.CharField(label='Add information, related to the tag:', max_length=50)
    tag = forms.ModelChoiceField(queryset=Tag.objects.all())
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all())

    class Meta:
        model = Value
        fields = [
            'name',
            'tag',
        ]

# checkboxes django
# form /
# fbv
# просто без формы попробовать
