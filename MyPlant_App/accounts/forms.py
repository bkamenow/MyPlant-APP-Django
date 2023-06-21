from django import forms

from MyPlant_App.accounts.models import UserModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ('profile_picture',)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance
