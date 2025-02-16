from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ncard_app import models
from ncard_app.views.resources import (AwardResource, EventResource,
                                       PublicationResource, OrganisationResource,
                                       PersonResource, StudentResource, DepartmentResource)

admin.site.register(models.Country)


class GrantInvestigatorInline(admin.TabularInline):
    model = models.GrantInvestigator
    fields = ['investigator', 'chief']
    extra = 1


class GrantAdmin(ImportExportModelAdmin):
    list_display = (
        "title", "grant_reference", "roap_reference", 'agency', "project", 'status', 'year_submitted', 'year_start',
        'year_end', 'bu_no', 'pg_no', 'total_request', 'total_award')
    inlines = [
        GrantInvestigatorInline
    ]
    exclude = ['investigators']


admin.site.register(models.Grant, GrantAdmin)


class DepartmentInline(admin.TabularInline):
    model = models.Department
    fields = ['name']
    extra = 1


class OrganisationAdmin(ImportExportModelAdmin):
    resource_classes = [OrganisationResource]
    list_display = ("name", "primary_contact", "phone", "website", "twitter_handle", "organisation_type")
    inlines = [
        DepartmentInline
    ]

    pass


admin.site.register(models.Organisation, OrganisationAdmin)


class DepartmentAdmin(ImportExportModelAdmin):
    resource_classes = [DepartmentResource]
    list_display = ('name', 'org')

    pass


admin.site.register(models.Department, DepartmentAdmin)


class EventAdmin(ImportExportModelAdmin):
    list_display = ("title", "event_type", "date", "number_attendees", "detail", "lead_organisation", "location")
    resource_classes = [EventResource]
    pass


admin.site.register(models.Event, EventAdmin)


class PublicationAdmin(ImportExportModelAdmin):
    list_display = (
        "title", "publication_type", "ncard_publication", "year", "journal", "journal_ISSN", "volume", "issue",
        "page_start", "page_end", "open_access_status", "doi", "electronic_ISBN", "print_ISBN", "citation")
    resource_classes = [PublicationResource]
    pass


admin.site.register(models.Publication, PublicationAdmin)


class StudentsAdmin(ImportExportModelAdmin):
    list_displays = (
        'student_name', 'student_type', 'supervisor', 'active_student', 'title_topic', 'year_start', 'year_end',
        'scholarship', 'notes')
    resource_classes = [StudentResource]
    pass


admin.site.register(models.Students, StudentsAdmin)


class AwardAdmin(ImportExportModelAdmin):
    list_displays = ('award_type', 'agency', 'name', 'recipients', 'status', 'detail', 'year', 'no_year', 'link')
    resource_classes = [AwardResource]
    pass


admin.site.register(models.Award, AwardAdmin)


class ProjectAdmin(ImportExportModelAdmin):
    list_displays = ('name', 'lead', 'status', 'funded')
    pass


admin.site.register(models.Project, ProjectAdmin)


class PersonAdmin(ImportExportModelAdmin):
    list_displays = (
        'title', 'given_name', 'middle_name', 'surname', 'surname_first', 'active', 'email', 'email2', 'phone_office',
        'phone_mobile', 'phone_home', 'cre_role', 'ncard_relation', 'project', 'display_on_website', 'profile_url',
        'orcid_id', 'scopus_id', 'wos_researcher_id', 'google_scholar', 'researchgate', 'loop_profile', 'linkedin',
        'twitter', 'location', 'organisation_primary', 'organisation_other', 'clinician', 'research_focus',
        'work_line1',
        'work_line2', 'work_line3', 'work_suburb', 'work_state', 'work_postcode', 'work_country', 'home_line1',
        'home_line2', 'home_line3', 'home_suburb', 'home_state', 'home_postcode', 'home_country', 'notes')
    resource_classes = [PersonResource]
    pass


admin.site.register(models.Person, PersonAdmin)
