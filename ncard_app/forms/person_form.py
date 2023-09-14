from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, HTML
from django.forms import ModelForm

from ncard_app import models


class PersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'
        exclude = ['id', 'surname_first', 'auth_user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "person"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['department_primary'].queryset = models.Department.objects.none()

        if "organisation_primary" in self.data:
            try:
                organisation_primary_id = int(self.data.get("organisation_primary"))
                self.fields["department_primary"].queryset = models.Department.objects.filter(
                    organisation_id=organisation_primary_id).order_by("name")
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Department queryset
        elif self.instance.pk:
            self.fields["department_primary"].queryset = models.Department.objects.filter(
                org=self.instance.organisation_primary).order_by('name')

        self.fields['department_other'].queryset = models.Department.objects.none()

        if "organisation_other" in self.data:
            try:
                organisation_other_id = int(self.data.get("organisation_other"))
                self.fields["department_other"].queryset = models.Department.objects.filter(
                    org=organisation_other_id).order_by("name")
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Department queryset
        elif self.instance.pk:
            self.fields["department_other"].queryset = models.Department.objects.filter(
                org=self.instance.organisation_other).order_by('name')

        self.helper.layout = Layout(
            TabHolder(
                Tab('Contact Details',
                    HTML("<br>"),
                    Row(
                        Column('title', css_class='col-md-1 mb-0'),
                        Column('given_name', css_class='col-md-4 mb-0'),
                        Column('middle_name', css_class='col-md-3 mb-0'),
                        Column('surname', css_class='col-md-4 mb-0'),
                    ),
                    Row('active'),
                    Row(
                        Column('email'),
                        Column('email2'),
                    ),
                    Row(
                        Column('phone_office'),
                        Column('phone_mobile'),
                        Column('phone_home'),
                    ),
                    ),

                Tab('NCARD Info',
                    HTML("<br>"),
                    Row(
                        Column('cre_role', css_class='col-md-4 mb-0'),
                        Column('ncard_relation', css_class='col-md-4 mb-0'),
                    ),
                    Row(Field('project', css_class='selectpicker form-control row', data_live_search='true')),
                    Row(
                        Column('display_on_website', css_class='col-md-3 mb-0'),
                        Column('profile_url', css_class='col-md-9 mb-0'),
                    ),
                    ),

                Tab('Researcher Profile',
                    HTML("<br>"),
                    Row(
                        Column('clinician', css_class='col-md-2 mb-0'),
                        Column('research_focus', css_class='col-md-10 mb-0'),
                    ),
                    Row(
                        Column('orcid_id', css_class='col-md-4 mb-0'),
                        Column('scopus_id', css_class='col-md-4 mb-0'),
                        Column('wos_researcher_id', css_class='col-md-4 mb-0'),
                    ),
                    Row('google_scholar'),
                    Row('researchgate'),
                    Row('loop_profile'),
                    Row(
                        Column('linkedin', css_class='col-md-5 mb-0'),
                        Column('twitter', css_class='col-md-3 mb-0'),
                    ),
                    ),

                Tab('Organisational Info',
                    HTML("<br>"),
                    Row(Field('employers', css_class='selectpicker form-control', data_live_search='true')),
                    Row('location'),
                    Row('organisation_primary', css_class='selectpicker form-control', data_live_search='true'),
                    Row('department_primary', css_class='selectpicker form-control', data_live_search='true'),
                    Row('organisation_other', css_class='selectpicker form-control', data_live_search='true'),
                    Row('department_other', css_class='selectpicker form-control', data_live_search='true'),
                    ),

                Tab('Office Address',
                    HTML("<br>"),
                    Row('work_line1'),
                    Row('work_line2'),
                    Row('work_line3'),
                    Row(
                        Column('work_suburb', css_class='col-md-3 mb-0'),
                        Column('work_state', css_class='col-md-3 mb-0'),
                        Column('work_postcode', css_class='col-md-3 mb-0'),
                        Column('work_country', css_class='col-md-3 mb-0'),
                    ),
                    ),

                Tab('Home Address',
                    HTML("<br>"),
                    Row('home_line1'),
                    Row('home_line2'),
                    Row('home_line3'),
                    Row(
                        Column('home_suburb', css_class='col-md-3 mb-0'),
                        Column('home_state', css_class='col-md-3 mb-0'),
                        Column('home_postcode', css_class='col-md-3 mb-0'),
                        Column('home_country', css_class='col-md-3 mb-0'),
                    ),
                    ),

                Tab('Notes',
                    HTML("<br>"),
                    Row('notes'),
                    ),
            )
        )
