from django import forms
from django.contrib.auth.models import User
from .models import Task

from django import forms
from django.contrib.auth.models import User
from .models import Task

from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'due', 'user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        if not user.is_superuser:
            self.fields.pop('user')

        if user.is_superuser:
            self.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.all(),
                label="Assign To",
                required=False
            )

    def assignee(self, user):
        # Check if the user is the assignee
        return user == self.instance.user if self.instance else False

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        if self.assignee(user):
            # Set the 'Assigned By' field to the name of the person who assigned the task
            cleaned_data['assigned_by'] = self.instance.assigned_by if self.instance else ""
        return cleaned_data

