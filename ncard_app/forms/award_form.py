from django.forms import ModelForm
from ncard_app import models
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from crispy_forms.bootstrap import Tab, TabHolder

class AwardForm(ModelForm):
    class Meta:
        model = models.Award
        exclude = ["id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "award"
        self.helper = FormHelper(self)
        self.helper.form_tag = False

