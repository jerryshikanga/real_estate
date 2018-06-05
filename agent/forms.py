from django import forms
from django.contrib.auth.models import User
from .models import Agent


class AgentForm(forms.ModelForm) :
    class Meta :
        exclude = ('date_added', )


class AgentCreationForm(forms.Form) :
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    password1 = forms.CharField(label="Password", required=True, widget=forms.PasswordInput, max_length=30)
    password2 = forms.CharField(label="Password Confirm", required=True, widget=forms.PasswordInput, max_length=30)
    email = forms.EmailField(label="Email address", required=True)

    telephone = forms.IntegerField(label="Telephone", required=True)
    description = forms.CharField(label="Description", required=True)
    picture = forms.ImageField(label="Picture", required=True)

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password1'] != form_data.get('password2') :
            self.add_error("password1", "Passwords must match")
            self.add_error("password2", "Passwords must match")

            del form_data['password1']
            del form_data['password2']

        return form_data

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name= self.cleaned_data['last_name']
        )
        user.set_password(self.cleaned_data['password1'])
        user.save()

        agent = Agent.objects.create(
            user=user,
            telephone=self.cleaned_data['telephone'],
            description=self.cleaned_data['description'],
            picture=self.cleaned_data['picture']
        )
        agent.save()

        return agent
