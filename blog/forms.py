from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blog.models import Subscribe


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        exclude = ()

