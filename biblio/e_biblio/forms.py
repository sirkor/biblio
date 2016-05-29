from django import forms
from e_biblio.models import Document


class DocumentAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(DocumentAddForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(DocumentAddForm, self).save(commit=False)
        instance.author = self.request.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Document
        exclude = ('author', )