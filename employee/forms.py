from django import forms
from .models import Employee
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('contact', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gender', css_class='form-group col-md-4 mb-0'),
                Column('role', css_class='form-group col-md-4 mb-0'),
                Column('salary', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )
    class Meta:
        model = Employee
        fields = '__all__'
