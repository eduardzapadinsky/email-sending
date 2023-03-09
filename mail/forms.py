from django import forms

from mail.models import ContactBase


class ContactBaseForm(forms.ModelForm):
    """
    Form for subscriber

    """
    class Meta:
        model = ContactBase
        fields = "__all__"
