from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
