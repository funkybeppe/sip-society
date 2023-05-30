from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        is_premium = kwargs.pop('is_premium', None)
        super().__init__(*args, **kwargs)

        if is_premium:
            self.fields['is_premium'] = True
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def clean_is_premium(self):
        """Method for assigning boolean value to is_premium field depending
        checkbox value"""
        premium = self.cleaned_data.get('is_premium', False)
        if premium:
            is_premium = True
        else:
            is_premium = False
        return is_premium
