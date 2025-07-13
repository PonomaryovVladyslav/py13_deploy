from django.forms import ModelForm

from notes.models import Note


class NoteCreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ('text',)