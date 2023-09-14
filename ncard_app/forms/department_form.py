from django.forms import ModelForm
from ncard_app import models
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML, Field
from crispy_forms.bootstrap import Tab, TabHolder


class DepartmentForm(ModelForm):
    class Meta:
        model = models.Department
        exclude = ["id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "department"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-9 mb-0'),
            ),
            Row(Field('org', css_class='selectpicker form-control row mb-0', data_live_search='true')),
        )
