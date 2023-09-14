from django.views import View
from crispy_forms.utils import render_crispy_form
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from ncard_app import forms, models
from django.contrib import messages


def load_departments_primary(request):
    organisation_id = request.GET.get('organisation_primary')
    departments = models.Department.objects.filter(org=organisation_id).order_by('name')
    return render(request, 'detail_views/department_dropdown_list_options.html', {'departments': departments})


def load_departments_other(request):
    organisation_id = request.GET.get('organisation_other')
    departments = models.Department.objects.filter(org=organisation_id).order_by('name')
    return render(request, 'detail_views/department_dropdown_list_options.html', {'departments': departments})


class PersonListView(ListView):
    model = models.Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    template_name = 'detail_views/add_person.html'
    form_class = forms.PersonForm

    def get_success_url(self):
        return reverse('list-people')


class PersonUpdateView(UpdateView):
    template_name = 'detail_views/edit_person.html'
    model = models.Person
    form_class = forms.PersonForm

    def get_success_url(self):
        return reverse('list-people')


class OrganisationListView(ListView):
    model = models.Organisation
    template_name = "detail_views/list-organisations.html"
    context_object_name = "orgs"


class OrganisationCreateView(CreateView):
    template_name = 'detail_views/add_organisation.html'
    form_class = forms.OrganisationForm

    def get_success_url(self):
        return reverse('list-organisations')


class OrganisationUpdateView(UpdateView):
    template_name = 'detail_views/edit_organisation.html'
    model = models.Organisation
    form_class = forms.OrganisationForm

    def get_success_url(self):
        return reverse('list-organisations')


class DepartmentCreateView(CreateView):
    template_name = "detail_views/add_department.html"
    form_class = forms.DepartmentForm

    def get_success_url(self):
        return reverse('list-departments')


class DepartmentUpdateView(UpdateView):
    template_name = 'detail_views/department.html'
    model = models.Department
    form_class = forms.DepartmentForm

    def get_success_url(self):
        return reverse('list-departments')


class AwardCreateView(CreateView):
    template_name = 'detail_views/add_award.html'
    form_class = forms.AwardForm

    def get_success_url(self):
        return reverse('list-awards')


class AwardUpdateView(UpdateView):
    template_name = 'detail_views/edit_award.html'
    model = models.Award
    form_class = forms.AwardForm

    def get_success_url(self):
        return reverse('list-awards')


class EventCreateView(CreateView):
    template_name = 'detail_views/add_event.html'
    form_class = forms.EventForm

    def get_success_url(self):
        return reverse('list-events')


class EventUpdateView(UpdateView):
    template_name = 'detail_views/edit_event.html'
    model = models.Event
    form_class = forms.EventForm

    def get_success_url(self):
        return reverse('list-events')


class ProjectCreateView(CreateView):
    template_name = 'detail_views/add_project.html'
    form_class = forms.ProjectForm

    def get_success_url(self):
        return reverse('list-projects')


class ProjectUpdateView(UpdateView):
    template_name = 'detail_views/edit_project.html'
    model = models.Project
    form_class = forms.ProjectForm

    def get_success_url(self):
        return reverse('list-projects')


class GrantCreateView(CreateView):
    template_name = 'detail_views/add_grant.html'
    form_class = forms.GrantForm

    def get_success_url(self):
        return reverse('list-grants')


class GrantUpdateView(UpdateView):
    template_name = 'detail_views/edit_grant.html'
    model = models.Grant
    form_class = forms.GrantForm

    def get_success_url(self):
        return reverse('list-grants')


class PublicationCreateView(CreateView):
    template_name = 'detail_views/add_publication.html'
    form_class = forms.PublicationForm

    def get_success_url(self):
        return reverse('list-publications')


class PublicationUpdateView(UpdateView):
    template_name = 'detail_views/edit_publication.html'
    model = models.Publication
    form_class = forms.PublicationForm

    def get_success_url(self):
        return reverse('list-publications')


class StudentCreateView(CreateView):
    template_name = 'detail_views/add_student.html'
    form_class = forms.StudentForm

    def get_success_url(self):
        return reverse('list-students')


class StudentUpdateView(UpdateView):
    template_name = 'detail_views/edit_student.html'
    model = models.Students
    form_class = forms.StudentForm

    def get_success_url(self):
        return reverse('list-students')
