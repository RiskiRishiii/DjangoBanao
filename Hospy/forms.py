from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "profile_picture",
            "address",
            "city",
            "state",
            "pin_code",
            "user_type"
        )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("password_mismatch")
        return cleaned_data
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
