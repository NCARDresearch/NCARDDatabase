from django.forms import ModelForm
from ncard_app import models
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML, Field
from crispy_forms.bootstrap import Tab, TabHolder

class GrantForm(ModelForm):
    class Meta:
        model = models.Grant
        exclude = ["id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "grant"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row('title'),
            Row(
                Column('grant_reference', css_class='col-md-4 mb-0'),
                Column('roap_reference',css_class='col-md-4 mb-0'),
                ),
            Row(Field('agency', css_class='selectpicker form-control row', data_live_search='true')),
            Row('project'),
            Row('status'),
            Row(Field('investigators', css_class='selectpicker form-control row mb-0', data_live_search='true')),
            Row(
                Column('year_submitted', css_class='col-md-2 mb-0'),
                Column('year_start', css_class='col-md-2 mb-0'),
                Column('year_end', css_class='col-md-2 mb-0'),
                ),
            Row(
                Column('bu_no', css_class='col-md-3 mb-0'),
                Column('pg_no', css_class='col-md-3 mb-0'),
                ),
            Row(
                Column('total_request', css_class='col-md-3 mb-0'),
                Column('total_award', css_class='col-md-3 mb-0'),
                ),
            )
