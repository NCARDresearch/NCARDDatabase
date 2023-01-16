from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, CharWidget

from ncard_app.models import (Award, Event, Grant, Organisation, Person,
                              Project, Publication, Students)


class OrganisationResource(resources.ModelResource):

    class Meta:
        model = Organisation
        import_id_fields=('name')

class PersonResource(resources.ModelResource):
    organisation_primary = fields.Field(
        column_name='organisation_primary',
        attribute='organisation_primary',
        widget=ForeignKeyWidget(Organisation,'name'
                                )
        )
    organisation_other = fields.Field(
        column_name='organisation_primary',
        attribute='organisation_primary',
        widget=ForeignKeyWidget(Organisation,'name'
                                )
        )
    title_1 = fields.Field(
        attribute='title_1',
        column_name='title',
        widget=CharWidget(),
        default=''
        )
    mid_name = fields.Field(
        attribute='mid_name',
        column_name='middle_name',
        widget=CharWidget(),
        default=''
        )
    phone_off = fields.Field(
        attribute='phone_off',
        column_name='phone_office',
        widget=CharWidget(),
        default=''
        )
    class Meta:
        model = Person

class ProjectResource(resources.ModelResource):
    lead = fields.Field(
        column_name='lead',
        attribute='lead',
        widget=ForeignKeyWidget(Person, 'given_name'
                                )
        )
    class Meta:
        model = Project

class AwardResource(resources.ModelResource):
    agency = fields.Field(
        column_name='agency',
        attribute='agency',
        widget=ForeignKeyWidget(Organisation, 'name'
                                )
        )
    recipients = fields.Field(
        column_name='recipients',
        attribute='recipients',
        widget=ManyToManyWidget(Person, field='given_name'
                                )
        )
    class Meta:
        model = Award

class EventResource(resources.ModelResource):
    lead_organisation = fields.Field(
        column_name='lead_organisation',
        attribute='lead_organisation',
        widget=ForeignKeyWidget(Organisation,'name'
                                )
        )
    class Meta:
        model = Event

class PublicationResource(resources.ModelResource):
    class Meta:
        model = Publication

class GrantResource(resources.ModelResource):
    class Meta:
        model = Grant    

class StudentResource(resources.ModelResource):
    class Meta:
        model = Students
        title_top = fields.Field(
            attribute='title_top',
            column_name='title_topic',
            widget=CharWidget(),
            default=''
            )
