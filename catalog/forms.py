from django import forms
from catalog.models import Product, Version


class VersionForm(forms.ModelForm):

    current_version = forms.BooleanField(
        required=False,
        label='Активная версия',
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'}),
    )

    class Meta:
        model = Version
        fields = ('version_number', 'version_title', 'current_version',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['current_version'].widget.attrs['class'] = 'checkbox-left'


class ProductForm(forms.ModelForm):

    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа',
                       'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')

        for word in self.FORBIDDEN_WORDS:
            if word == cleaned_data.lower() or word in cleaned_data.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово {word}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for word in self.FORBIDDEN_WORDS:
            if word == cleaned_data.lower() or word in cleaned_data.lower():
                raise forms.ValidationError(f'Описание содержит запрещенное слово "{word}"')
        return cleaned_data

