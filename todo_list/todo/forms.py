from django.forms import ModelForm
from .models import ToDo

# Manually created python file
class TodoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description', 'important']
