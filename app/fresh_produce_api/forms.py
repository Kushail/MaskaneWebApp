from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Product


class QuoteForm(forms.Form):
    """Form to submit and return a qoute"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))
 
    product = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        label="Product name",
    )
    quantity = forms.FloatField(

    )
