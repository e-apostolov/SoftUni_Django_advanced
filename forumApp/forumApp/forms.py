from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from forumApp.accounts.models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')