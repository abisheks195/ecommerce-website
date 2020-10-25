from django import forms
from django.contrib.auth import get_user_model

User = get_user_model();

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fullname'}));
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}));
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}));

    # def clean_email(self):
    #     email = self.cleaned_data.get('email');
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError('Email has to be gmail.com');
    #     return email;

    # def clean_content(self):
    #     raise forms.ValidationError('Content is wrong!');


class LoginForm(forms.Form):
     username = forms.CharField();
     password = forms.CharField(widget=forms.PasswordInput);

class RegisterForm(forms.Form):
    username = forms.CharField();
    email = forms.EmailField();
    password = forms.CharField(widget=forms.PasswordInput);
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput);

    def clean_username(self):
        username = self.cleaned_data.get('username');
        qs = User.objects.filter(username=username);
        if qs.exists():
            raise forms.ValidationError("Username already exists");
        return username;

    def clean_email(self):
        email = self.cleaned_data.get('email');
        qs = User.objects .filter(email=email);
        if qs.exists():
            raise forms.ValidationError("Email already exists");
        return email;

    def clean(self):
        password = self.cleaned_data.get('password');
        password2 = self.cleaned_data.get('password2');
        if password2 != password:
            raise forms.ValidationError('Passwords do not match!');
        return self.cleaned_data;
