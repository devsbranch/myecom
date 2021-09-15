from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    genda=forms.CharField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        def save(self,commit=True):
            super(CreateUserForm, self).save(commit=False)
            self.user.email = self.cleaned_data['email']
            if commit:
             User.save()
             return User
