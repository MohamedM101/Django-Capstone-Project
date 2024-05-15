from django import forms
from .models import Topic, Entry
class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('text', 'entry_image')
		labels = {'text': '','entry_image': '',}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
