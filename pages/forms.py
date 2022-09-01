from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class DefaultUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields


class DefaultUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
