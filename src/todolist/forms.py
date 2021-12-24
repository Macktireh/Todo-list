from django import forms
from todolist.models import Task


class FormTask(forms.ModelForm):
	tache = forms.CharField(max_length=200,
		widget=forms.TextInput(attrs={
			'placeholder': 'Entrer votre tâche',
			'class': 'input-tache'
			}))

	class Meta:
		model = Task
		fields = [
			'tache',
		]