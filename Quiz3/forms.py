from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your First Name',
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Last Name',
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address',
        }
    ))

    phone_number = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your First Name',
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your First Name',
        }
    ))