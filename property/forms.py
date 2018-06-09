from  django import forms
from property.models import PropertyEnquiry


class PropertyForm (forms.ModelForm) :
    class Meta :
        exclude = ('date_added',)


class PropertyTypeForm(forms.ModelForm) :
    class Meta :
        exclude = ()


class EnquiryForm(forms.Form) :
    subject = forms.CharField(required=True, )
    message = forms.CharField(required=True, widget=forms.Textarea)

    def save_inquiry(self, user, property):
        inquiry = PropertyEnquiry.objects.create(
            user=user,
            property=property,
            message=self.data['message'],
            subject=self.data['subject'],
        )
        inquiry.save()