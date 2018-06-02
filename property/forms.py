from  django import forms


class PropertyForm (forms.ModelForm) :
    class Meta :
        exclude = ('date_added',)


class PropertyTypeForm(forms.ModelForm) :
    class Meta :
        exclude = ()