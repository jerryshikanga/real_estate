from django import forms


class AgentForm(forms.ModelForm) :
    class Meta :
        exclude = ('date_added')