from django import forms

from MyPlant_App.plants.models import PlantModel


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
