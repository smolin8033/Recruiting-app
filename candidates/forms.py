from django import forms

from candidates.models import Candidate, Tag, Value


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TagCreateForm(forms.ModelForm):
    name = forms.CharField(label='Add info tag:', max_length=50)
    values = forms.ModelMultipleChoiceField(
        queryset=Value.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Tag
        fields = ['name', 'values']


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
