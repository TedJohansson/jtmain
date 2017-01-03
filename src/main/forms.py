from django import forms
from django.forms import Form, ModelForm, ValidationError
from .models import Post
from django.contrib.auth import authenticate, login


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PostForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        We need to do some model validation to ensure the User given is acceptable.

        We also need to make sure we actually have a file.

        :return: dict, the data needed for the model.
        """

        cleaned_data = super(PostForm, self).clean()
        cleaned_data['author'] = self.user

        return cleaned_data


class LoginForm(Form):
    """
    Manage logins to the app.
    """
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        """
        Make sure the login worked.

        :return: dict, the cleaned_data.
        """
        user = self.login()

        if not user or not user.is_active:
            raise ValidationError('Sorry that was an invalid login. Please try again.')

        return self.cleaned_data

    def login(self):
        """
        Authenticate the user for logging in.

        :return: User, the authenticated user.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        return user
