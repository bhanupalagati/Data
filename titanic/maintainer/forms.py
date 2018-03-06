from django.forms import ModelForm
from maintainer.models import details

class details_form(ModelForm):
    class Meta:
        model = details
        fields = '__all__'
