from import_export import fields, resources
from import_export.widgets import (ForeignKeyWidget, ManyToManyWidget,
                                   CharWidget, DecimalWidget)

from ncard_app.models import (Award, Event, Grant, Organisation, Person,
                              Project, Publication, Students)


class OrganisationResource(resources.ModelResource):
    phone = fields.Field(
        attribute='phone',
        column_name='phone',
        widget=CharWidget(),
        default=''
        )
    twitter_handle = fields.Field(
        attribute='twitter_handle',
        column_name='twitter_handle',
        widget=CharWidget(),
        default=''
        )
    class Meta:
        model = Organisation
        import_id_fields = ('name',)
        export_order = ('id','name','organisation_type','primary_contact',
                        'phone','website','twitter_handle')

class PersonResource(resources.ModelResource):
    organisation_primary = fields.Field(
        column_name='organisation_primary',
        attribute='organisation_primary',
        widget=ForeignKeyWidget(Organisation,'id'
                                )
        )
    organisation_other = fields.Field(
        column_name='organisation_other',
        attribute='organisation_other',
        widget=ForeignKeyWidget(Organisation,'id'
                                )
        )
    title = fields.Field(
        attribute='title',
        column_name='title',
        widget=CharWidget(),
        default=''
        )
    middle_name = fields.Field(
        attribute='middle_name',
        column_name='middle_name',
        widget=CharWidget(),
        default=''
        )
    phone_office = fields.Field(
        attribute='phone_office',
        column_name='phone_office',
        widget=CharWidget(),
        default=''
        )
    phone_mobile = fields.Field(
        attribute='phone_mobile',
        column_name='phone_mobile',
        widget=CharWidget(),
        default=''
        )
    phone_home = fields.Field(
        attribute='phone_home',
        column_name='phone_home',
        widget=CharWidget(),
        default=''
        )
    cre_role = fields.Field(
        attribute='cre_role',
        column_name='cre_role',
        widget=CharWidget(),
        default=''
        )
    project = fields.Field(
        attribute='project',
        column_name='project',
        widget=ManyToManyWidget(Person, 'id'
                          )
        )
    profile_url = fields.Field(
        attribute='profile_id',
        column_name='profile_id',
        widget=CharWidget(),
        default=''
        )
    orcid_id = fields.Field(
        attribute='orcid_id',
        column_name='orcid_id',
        widget=CharWidget(),
        default=''
        )
    wos_researcher_id = fields.Field(
        attribute='wos_researcher_id',
        column_name='wos_researcher_id',
        widget=CharWidget(),
        default=''
        )
    twitter = fields.Field(
        attribute='twitter',
        column_name='twitter',
        widget=CharWidget(),
        default=''
        )
    location = fields.Field(
        attribute='location',
        column_name='location',
        widget=CharWidget(),
        default=''
        )
    research_focus = fields.Field(
        attribute='research_focus',
        column_name='research_focus',
        widget=CharWidget(),
        default=''
        )
    work_line1 = fields.Field(
        attribute='work_line1',
        column_name='work_line1',
        widget=CharWidget(),
        default=''
        )
    work_line2 = fields.Field(
        attribute='work_line2',
        column_name='work_line2',
        widget=CharWidget(),
        default=''
        )
    work_line3 = fields.Field(
        attribute='work_line3',
        column_name='work_line3',
        widget=CharWidget(),
        default=''
        )
    work_suburb = fields.Field(
        attribute='work_suburb',
        column_name='work_suburb',
        widget=CharWidget(),
        default=''
        )
    work_state = fields.Field(
        attribute='work_state',
        column_name='work_state',
        widget=CharWidget(),
        default=''
        )
    work_postcode = fields.Field(
        attribute='work_postcode',
        column_name='work_postcode',
        widget=CharWidget(),
        default=''
        )
    home_line1 = fields.Field(
        attribute='home_line1',
        column_name='home_line1',
        widget=CharWidget(),
        default=''
        )
    home_line2 = fields.Field(
        attribute='home_line2',
        column_name='home_line2',
        widget=CharWidget(),
        default=''
        )
    home_line3 = fields.Field(
        attribute='home_line3',
        column_name='home_line3',
        widget=CharWidget(),
        default=''
        )
    home_suburb = fields.Field(
        attribute='home_suburb',
        column_name='home_suburb',
        widget=CharWidget(),
        default=''
        )
    home_state = fields.Field(
        attribute='home_state',
        column_name='home_state',
        widget=CharWidget(),
        default=''
        )
    home_postcode = fields.Field(
        attribute='home_postcode',
        column_name='home_postcode',
        widget=CharWidget(),
        default=''
        )
    notes = fields.Field(
        attribute='notes',
        column_name='notes',
        widget=CharWidget(),
        default=''
        )
   
    class Meta:
        model = Person
        export_order = ('id','title','given_name','middle_name','surname',
                        'surname_first','active','auth_user','email','email2',
                        'phone_office','phone_mobile','phone_home','cre_role',
                        'ncard_relation','project','display_on_website',
                        'profile_url','orcid_id','scopus_id',
                        'wos_researcher_id','google_scholar','researchgate',
                        'loop_profile','linkedin','twitter','employers',
                        'location','organisation_primary','organisation_other',
                        'clinician','research_focus','work_line1','work_line2',
                        'work_line3','work_suburb','work_state','work_postcode',
                        'work_country','home_line1','home_line2','home_line3',
                        'home_suburb','home_state', 'home_postcode',
                        'home_country','notes')

class ProjectResource(resources.ModelResource):
    lead = fields.Field(
        column_name='lead',
        attribute='lead',
        widget=ForeignKeyWidget(Person, 'id'
                                )
        )
    class Meta:
        model = Project
        export_order = ('id','name','lead','status','funded')

class AwardResource(resources.ModelResource):
    agency = fields.Field(
        column_name='agency',
        attribute='agency',
        widget=ForeignKeyWidget(Organisation, 'id'
                                )
        )
    recipients = fields.Field(
        column_name='recipients',
        attribute='recipients',
        widget=ManyToManyWidget(Person, 'id'
                                )
        )
    no_year = fields.Field(
        attribute='no_year',
        column_name='no_year',
        widget=DecimalWidget(),
        default=0.0
        )
    detail = fields.Field(
        attribute='detail',
        column_name='detail',
        widget=CharWidget(),
        default=''
        )
    class Meta:
        model = Award
        export_order = ('id','award_type', 'agency','name', 'recipients',
                        'status','detail', 'year', 'no_year', 'link')

class EventResource(resources.ModelResource):
    lead_organisation = fields.Field(
        column_name='lead_organisation',
        attribute='lead_organisation',
        widget=ForeignKeyWidget(Organisation,'id'
                                )
        )
    title = fields.Field(
        attribute='title',
        column_name='title',
        widget=CharWidget(),
        default=''
        )
    event_type = fields.Field(
        attribute='event_type',
        column_name='event_type',
        widget=CharWidget(),
        default=''
        )
    location = fields.Field(
        attribute='location',
        column_name='location',
        widget=CharWidget(),
        default=''
        )
    number_attendees = fields.Field(
        attribute='number_attendees',
        column_name='number_attendees',
        widget=CharWidget(),
        default=''
        )
    participants = fields.Field(
        attribute='participants',
        column_name='participants',
        widget=CharWidget(),
        default=''
        )
    details = fields.Field(
        attribute='details',
        column_name='details',
        widget=CharWidget(),
        default=''
        )
    class Meta:
        model = Event
        export_order = ('id',"event_type", "date", "number_attendees", "title",
                        "detail", "lead_organisation", "location")

class PublicationResource(resources.ModelResource):
    page_start = fields.Field(
        attribute='page_start',
        column_name='page_start',
        widget=CharWidget(),
        default=''
        )
    page_end = fields.Field(
        attribute='page_end',
        column_name='page_end',
        widget=CharWidget(),
        default=''
        )
    electronic_ISBN = fields.Field(
        attribute='electronic_ISBN',
        column_name='electronic_ISBN',
        widget=CharWidget(),
        default=''
        )
    print_ISBN = fields.Field(
        attribute='print_ISBN',
        column_name='print_ISBN',
        widget=CharWidget(),
        default=''
        )
    abstract = fields.Field(
        attribute='abstract',
        column_name='abstract',
        widget=CharWidget(),
        default=''
        )
    citation = fields.Field(
        attribute='citation',
        column_name='citation',
        widget=CharWidget(),
        default=''
        )
    source_ID = fields.Field(
        attribute='source_ID',
        column_name='source_ID',
        widget=CharWidget(),
        default=''
        )
    class Meta:
        model = Publication
        export_order = ('id',"title","publication_type","ncard_publication",
                        "year",'contributors',"journal","journal_ISSN","volume",
                        "page_start","page_end","open_access_status","doi",
                        "electronic_ISBN","print_ISBN","abstract","citation",
                        "source_ID")

class GrantResource(resources.ModelResource):
    grant_reference = fields.Field(
        attribute='grant_reference',
        column_name='grant_reference',
        widget=CharWidget(),
        default=''
        )
    roap_reference = fields.Field(
        attribute='roap_reference',
        column_name='roap_reference',
        widget=CharWidget(),
        default=''
        )
    bu_no = fields.Field(
        attribute='bu_no',
        column_name='bu_no',
        widget=CharWidget(),
        default=''
        )
    pg_no = fields.Field(
        attribute='pg_no',
        column_name='pg_no',
        widget=CharWidget(),
        default=''
        )
    total_request = fields.Field(
        attribute='total_request',
        column_name='total_request',
        widget=DecimalWidget(),
        default=0.0
        )
    total_award = fields.Field(
        attribute='total_award',
        column_name='total_award',
        widget=DecimalWidget(),
        default=0.0
        )
    class Meta:
        model = Grant
        export_order = ('id',"title", "grant_reference","roap_reference",'agency',"project",'status','investigators','year_submitted', 'year_start','year_end','bu_no', 'pg_no', 'total_request','total_award')

class StudentResource(resources.ModelResource):
    title_topic = fields.Field(
        attribute='title_topic',
        column_name='title_topic',
        widget=CharWidget(),
        default=''
        )
    scholarship = fields.Field(
        attribute='scholarship',
        column_name='scholarship',
        widget=ManyToManyWidget(Award, 'id'
                                )
        )
    notes = fields.Field(
        attribute='notes',
        column_name='notes',
        widget=CharWidget(),
        default=''
        )
    
    class Meta:
        model = Students
        export_order = ('id','student_name','student_type','supervisor',
                        'active_student','title_topic','year_start','year_end',
                        'scholarship','notes')
